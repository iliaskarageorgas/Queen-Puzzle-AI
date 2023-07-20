import sys
import time
from GeneticAlgorithm import GeneticAlgorithm

def main():
    # Getting the information necessary from the command line
    if len(sys.argv) != 5:
        sys.exit("Usage: python Queen_Puzzle.py {integer N} {integer P} {float M} {integer S}")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Not an integer")

    try:
        P = int(sys.argv[2])
    except ValueError:
        print("Not an integer")
    
    try:
        M = float(sys.argv[3])
    except ValueError:
        print("Not a float")
    
    try:
        S = int(sys.argv[4])
    except ValueError:
        print("Not an integer")

    # Calculating the minimum acceptable fitness
    minimumFitness = 0
    for i in range(N):
        minimumFitness += i

    start_time = time.time()
    genetic = GeneticAlgorithm(N)
    chromosome = genetic.runAlgorithm(P, M, S, minimumFitness)
    end_time = time.time()
    chromosome.print()
    print("Total time:", round(end_time - start_time, 3), "seconds")


main()