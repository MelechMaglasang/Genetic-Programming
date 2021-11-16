import ExpressionTree
import Node
import random
import copy
import math
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
import csv
import os.path




class GeneticProgramming:

        
        
    def crossOver(self, treeA, treeB,data):
        depthA = treeA.findDepth()
        depthB = treeB.findDepth()

        #Maybe we an just do a deep copy here?
        # newTreeA = treeA.cloneTree()

        # newTreeB = treeB.cloneTree()
        newTreeA = copy.deepcopy(treeA)
        newTreeB = copy.deepcopy(treeB)

        # crossDepthA = random.randint(1, depthA)
        if (depthA >= 2):
            crossPointsA = newTreeA.grabNodesAtDepth(random.randint(1,depthA-1))
        else:
            crossPointsA = [newTreeA.root]
        if (depthB >= 2):
            crossPointsB = newTreeB.grabNodesAtDepth(random.randint(1,depthB-1))
        else:
            crossPointsB = [newTreeB.root]

        #Bug, just return the parents
        # try:
        crossingA = random.choice(crossPointsA)

        crossingB = random.choice(crossPointsB)
        # except:
     
        #     return (treeA, treeB)

        if (depthB == 1 or depthA == 1):
            if (depthA == depthB):
                return (newTreeB, newTreeA)

            if (depthA == 1):
                if (random.randint(1, 2) == 1):
                    temp = copy.copy(crossingB.leftChild)
                    crossingB.leftChild = copy.copy(crossingA)
                    newTreeA.root = temp
            
                else:
                    temp = copy.copy(crossingB.rightChild)

                    crossingB.rightChild = copy.copy(crossingA)
                    newTreeA.root = temp

            elif (depthB == 1):
                if (random.randint(1, 2) == 1):
                    temp = copy.copy(crossingA.leftChild)

                    crossingA.leftChild = copy.copy(crossingB)
                    newTreeB.root = temp
            
                else:
                    temp = copy.copy(crossingA.rightChild)

                    crossingA.rightChild = copy.copy(crossingB)
                    newTreeB.root = temp

        else:

            if (random.randint(1, 2) == 1):
                crossingA.leftChild, crossingB.leftChild = crossingB.leftChild, crossingA.leftChild
            
            else:
                crossingA.rightChild, crossingB.rightChild = crossingB.rightChild, crossingA.rightChild

        newTreeA.fitness = newTreeA.findFitness(data)
        newTreeB.fitness = newTreeB.findFitness(data)
            
        return (newTreeA, newTreeB)


    def mutate(self, tree,data):
        depth = tree.findDepth()


        newTree = copy.deepcopy(tree)

        mutagen = Node.Node()
        leftLeaf = Node.Node()
        rightLeaf = Node.Node()

        mutagen.leftChild = leftLeaf
        mutagen.rightChild = rightLeaf

        mutagen.nodeValue = random.sample(mutagen.operands, 1)[0] 

        if (random.randint(1, 3) != 1):
            leftLeaf.nodeValue = "x"
        else:
            leftLeaf.nodeValue = random.sample(leftLeaf.leafVals, 1)[0]

        if (random.randint(1, 3) != 1):
            rightLeaf.nodeValue = "x"
        else:
            rightLeaf.nodeValue = random.sample(rightLeaf.leafVals, 1)[0]

        #For the leafs
        if (depth == 1):
            mutatee = newTree.root
        else:
            mutatee = random.choice(newTree.grabNodesAtDepth(depth - 1))

        if (random.randint(1, 2) == 1):
                
            mutatee.leftChild = mutagen
        
        else:
            mutatee.rightChild = mutagen

        # newTree.expression = newTree.toString()
        newTree.fitness = newTree.findFitness(data)
            
        return newTree

    def tournamentSelection(self, population):
        # print (len(population) / 5)
        samplePop1 = random.sample(population, int(len(population) * .1 ))
        samplePop2 = random.sample(population, int(len(population) * .1 ))


        winners = []

        winners.append(min(samplePop1, key = lambda t: t.fitness))
        winners.append(min(samplePop2, key = lambda t: t.fitness))
     

        return winners

        

    def symbReg(self, size, gens, data, noise):

        population = []

        for i in range (size):
            tree = ExpressionTree.ExpressionTree(data)

            population.append(tree)


        #Set Parameters:
        numMutate = size * 0.025
        numCarryOver = (size * 0.05) - 1 #Accounts for best ever tree

        print(numMutate, numCarryOver)
        
        bestEver = None

        filename = "dataset1runs"
        fileExists = os.path.isfile(filename)
        with open (filename, 'a') as csvfile:
            
            writer = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

            writer.writerow("RUN")
            
            for m in range(gens):
                print(m)

                newPopulation = []

                #Saving space for BestEver, top 8, and 5 mutatees. Must change if changing starting pop
                while (len(newPopulation) < (size - (numMutate + numCarryOver))):
                    
                    champions = self.tournamentSelection(population)

                    childTrees = self.crossOver(champions[0], champions[1],data)

                    for child in childTrees:
                        newPopulation.append(child)

                
                bestInGeneration = min(population, key = lambda t: t.fitness)

                population.pop(population.index(bestInGeneration))

                if (bestEver == None or bestEver.fitness > bestInGeneration.fitness):
                    bestEver = bestInGeneration
                newPopulation.append(bestEver)
                
                for i in range(math.ceil(numCarryOver)):
                    curr = min(population, key = lambda t: t.fitness)

                    population.pop(population.index(curr))
                    newPopulation.append(curr)
                
                randoMutates = random.sample(newPopulation, math.ceil(numMutate))

                for tree in randoMutates:
                
                    mutatee = self.mutate(tree, data)
                    newPopulation.append(mutatee)
                
                population = newPopulation

                #Fix ceil operation and cull the worst
                while (len(population) > size):
                    worstInGen = max(population, key = lambda t: t.fitness)
                    population.pop(population.index(worstInGen))

                print(len(population))

                minnie = min(population, key = lambda t: t.fitness)
                if (minnie.fitness < noise**2):
                    break
                writer.writerow({m, minnie.fitness, minnie.toString()})
                
        return min(population, key = lambda t: t.fitness)




def main():

    # np.random.seed(0)

    n_samples = 500
    
    #Doesn't really do well with constant values for Y, I think it has something to do with the tree structure for low nodes that resolve to 0
    X = np.random.randint(0, 100, n_samples)
    Y =  -1*X**2  + np.random.normal(loc=50, scale=250, size=(n_samples))
    # X = np.random.randint(-1, 80, n_samples)
    # Y = 1000*np.sin(.05*X) + np.random.normal(scale=50, size=(n_samples))

    data = np.column_stack((X,Y))
    

    trainingSet, testSet = train_test_split(data, test_size=0.2)


    player = GeneticProgramming()

    #Size of forest, generations, data, noise)
    winner = player.symbReg(100, 100, trainingSet, 250)

    print (winner.toString())
    print(winner.fitness)

    print("Test Set")
    print(winner.findFitness(testSet))


    filename = "dataset1runs"
    fileExists = os.path.isfile(filename)
    with open (filename, 'a') as csvfile:
            
        writer = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow({"winner", winner.fitness, winner.toString()})
        writer.writerow({"Test", winner.findFitness(testSet)})
       
    
if __name__ == "__main__":
    main()


        




    


        