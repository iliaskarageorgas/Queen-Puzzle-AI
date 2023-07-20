import random
import copy
from Chromosome import Chromosome

class GeneticAlgorithm():

    def __init__(self, N):
        self.N = N
        # A list containing chromosomes
        self.population = None
        # Used to indicate how likely it is to choose a chromosome based on its fitness score
        # It contains the index of each chromosome in the population list as many times as the 
        # fitness score indicates
        self.frequency = None


    def initializePopulation(self, populationSize):
        # Initialize the popoulation by creating random chromosomes
        self.population = []
        for i in range(populationSize):
            chromosome = Chromosome(self.N)
            self.population.append(chromosome)

        self.updateFrequency()

    
    def updateFrequency(self):
        # Update the list that contains the indexes of the chromosomes of the population list
        # Add the index of each chromosome to the frequency list as many times as its fitness score
        self.frequency = []
        for i in range(len(self.population)):
            for j in range(self.population[i].getFitness()):
                self.frequency.append(i)


    def reproduce(self, x, y):
        # Generate a new chromosome based on the two that are given as arguments
        
        # Randomly choose the point where the parents will be intersected
        intersectionPoint = random.randint(0, self.N - 1)
        firstChild = []
        secondChild = []

        # The first child has the left side of the x chromosome 
        # and the second child has the left side of the y chromosome
        for i in range(intersectionPoint):
            firstChild.append(x.getGenes()[i])
            secondChild.append(y.getGenes()[i])
        
        # The first child also has the right side of the y chromosome
        # and the second child has the right side of the x chromosome
        for j in range(intersectionPoint, self.N):
            firstChild.append(y.getGenes()[j])
            secondChild.append(x.getGenes()[j])
        
        firstChromosome = Chromosome(self.N, True)
        firstChromosome.copyChromosome(firstChild)
        secondChromosome = Chromosome(self.N, True)
        secondChromosome.copyChromosome(secondChild)
        
        return firstChromosome, secondChromosome


    def runAlgorithm(self, populationSize, mutationProbability, maxSteps, minFitness):
        # Initialize the population
        self.initializePopulation(populationSize)
        for steps in range(maxSteps):
            # Initialize the new genarated population
            newPopulation = []
            for j in range(round(populationSize / 2)):
                # We choose two chromosomes from the population
                # The probability of selecting a chromosome is based on
                # the number of times its index is on the frequency list.
                # So it depends on its fitness score
                xIndex = self.frequency[random.randint(0, len(self.frequency) - 1)]
                xParent = self.population[xIndex]
                yIndex = self.frequency[random.randint(0, len(self.frequency) - 1)]
                # We can't use the same chromosome two times to generate a new one
                while xIndex == yIndex:
                    yIndex = self.frequency[random.randint(0, len(self.frequency) - 1)]

                yParent = self.population[yIndex]
                # Generate the children of the two chromosomes
                children = self.reproduce(xParent, yParent)

                # Mutate the children based on the mutation probability
                if (random.uniform(0, 1) < mutationProbability):
                    children[0].mutate()
                    children[1].mutate()

                # and add them to the new population
                newPopulation.append(children[0])
                newPopulation.append(children[1])

            self.population = copy.deepcopy(newPopulation)
            # We want to find the chromosome with the greatest fitness 
            maxFitness = 0
            bestChromosome = None
            for i in range(len(self.population)):
                if self.population[i].getFitness() > maxFitness:
                    maxFitness = self.population[i].getFitness()
                    bestChromosome = self.population[i]      

            # If the chromosome with the best fitness is acceptable return it
            if bestChromosome.getFitness() >= minFitness:
                return bestChromosome
                
            # Update the frequency list
            self.updateFrequency()
        
        return bestChromosome
            