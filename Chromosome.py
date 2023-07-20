import random

class Chromosome():

    def __init__(self, N, copy = False):
        self.N = N
        # Integer that holds the fitness score of the chromosome
        self.fitness = None
        
        if not copy:
            # Each position shows the vertical position of a queen in the corresponding column
            self.genes = []

            for i in range(self.N):
                self.genes.append(random.randint(0, self.N - 1))
            
            self.calculateFitness()
    

    def copyChromosome(self, genes):
        # Create a copy of the chromosome which is given as argument
        self.genes = []
        
        for i in range(len(genes)):
            self.genes.append(genes[i])
        
        self.calculateFitness()
    

    def calculateFitness(self):
        # Calculates the fitness score of the chromosome as the number 
        # of pairs of queens that are not threatened
        nonThreats = 0

        for i in range(len(self.genes)):
            for j in range(i+1, len(self.genes)):
                '''
                Check if there are no queens in the same row
                and whether there are no queens in the same diagonal

                abs(i - j) calculates the number of columns between two queens
                abs(self.genes[i] - self.genes[j]) calculates the number of rows between two queens
                if those two numbers are the same, the two queens are in the same diagonal
                '''
                if self.genes[i] != self.genes[j] and abs(i - j) != abs(self.genes[i] - self.genes[j]):
                    nonThreats += 1

        self.fitness = nonThreats


    def mutate(self):
        # Randomly change the position of a queen
        self.genes[random.randint(0, self.N - 1)] = random.randint(0, self.N - 1)
        self.calculateFitness()


    def getGenes(self):
        return self.genes
    

    def setGenes(self, genes):
        self.genes = genes


    def getFitness(self):
        return self.fitness


    def setFitness(self, fitness):
        self.fitness = fitness


    def print(self):
        print("Chromosome: |", end="")
        for i in range(len(self.genes)):
            print(self.genes[i], end="")
            print("|", end="")
        
        print(", Fitness: ", end="")
        print(self.fitness)

        print("------------------------------------")
        for i in range(len(self.genes)):
            for j in range(len(self.genes)):
                if self.genes[j] == i:
                    print("|Q", end="")
                else:
                    print("| ", end="")
                
            print("|")

        print("------------------------------------")
