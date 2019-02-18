import ExpressionTree
import Node
import random
import copy

#For csv parsing
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split




class GeneticProgramming:

    def __init__(self, numGen):
        self.numGen = numGen
        
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


        crossingA = random.choice(crossPointsA)

        crossingB = random.choice(crossPointsB)

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


        # newTreeA.expression = newTreeA.toString()
        # newTreeB.expression = newTreeB.toString()
            
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
        #Assuming data will be formatted in the way i want it to

        # print (len(population) / 5)
        sampleTree1 = random.sample(population, int(len(population) * .1 ))
        sampleTree2 = random.sample(population, int(len(population) * .1 ))



        # random.shuffle(sampleTrees)



        # S = [1,2,3,4,5,6,7]
        
        # index = random.randint(1, len(sampleTrees)-1)
        # List1 = sampleTrees[index:]
        # List2 = sampleTrees[:index]

        # for tree in population:

        #     fitness = tree.findFitness(data)
        #     treeScorePair = (tree,fitness)

        #     if (bestHere == None or bestHere[1] > treeScorePair[1]):
        #         bestHere = treeScorePair
            

        #     bigData.append(treeScorePair)

        # n = int (len(population)/2)
  
        # using list comprehension 
        # final = [population[i * n:(i + 1) * n] for i in range((len(population) + n - 1) // n )]

        # print(final[0])

        winners = []
        # winners.append(sampleTree1)
        # winners.append(sampleTree2)
        winners.append(min(sampleTree1, key = lambda t: t.fitness))
        winners.append(min(sampleTree2, key = lambda t: t.fitness))
        # losers = []
        # for section in final:
        #     winners.append(min(section, key = lambda t: t.fitness))
            # losers.append(max(section, key = lambda t: t.fitness))


        # if (winners[0].fitness > winners[1].fitness):
        #     bestHere = winners[1]
        # else:
        #     bestHere = winners[0]
        # print ("winners",winners[0].fitness, winners[1].fitness)

        return winners

        

    def symbReg(self, size, gens, data):

        population = []

        for i in range (size):
            tree = ExpressionTree.ExpressionTree(data)

            population.append(tree)
        
        bestEver = None
        #Maybe do a while loop but for now im doing a for loop
        for m in range(gens):
            print(m)

            newPopulation = []

            while (len(newPopulation) <= 188):
                
                champions = self.tournamentSelection(population)

                childTrees = self.crossOver(champions[0], champions[1],data)

                for child in childTrees:
                    newPopulation.append(child)

                # for champ in champions:
                #     newPopulation.append(champ)
        
                # treesToMutate = random.sample(population, int (len(population) * .20 ))

            # for i in range(5):
            #     currTree = min(treesToMutate, key = lambda t: t.fitness)

            #     newTree = self.mutate(currTree,data)

            #     newPopulation.append(newTree)
            #     treesToMutate.pop(currTree)

            bestInGeneration = min(population, key = lambda t: t.fitness)

            population.pop(population.index(bestInGeneration))

            if (bestEver == None or bestEver.fitness > bestInGeneration.fitness):
                bestEver = bestInGeneration
            newPopulation.append(bestEver)


            for i in range(4):
                curr = min(population, key = lambda t: t.fitness)

                population.pop(population.index(curr))
                newPopulation.append(curr)

            randoMutates = random.sample(population, 5)

            for tree in randoMutates:
                # curr = min(population, key = lambda t: t.fitness)

                # population.pop(population.index(curr))
                mutatee = self.mutate(tree, data)
                newPopulation.append(mutatee)
            
            
            population = newPopulation
            
            minnie = min(population, key = lambda t: t.fitness)
            print (minnie.toString())
            print(minnie.fitness)


            # for i in range(len(champions)):
            #     currTree = champions[i][0]

            #     otherTrees = champions[:]

            #     otherTrees.pop(i)

            #     for j in range(len(otherTrees)):
            #         otherTree = champions[i][0]
                    
            #         for k in range(4):
            #             childrenTrees = self.crossOver(currTree, otherTree)

            #             for child in childrenTrees:
            #                 if (random.randint(1,1000) == 42):
            #                     mutatedChild = self.mutate(child)
            #                     newPopulation.append(mutatedChild)
            #                 else:
            #                     newPopulation.append(child)



            # #mate using the best ever seen
            # championTree = bestEver[0]

            # for i in range(len(champions)):
            #     otherTree = champions[i][0]

            #     childrenTrees = self.crossOver(championTree, otherTree)

            #     for child in childrenTrees:
            #         if (random.randint(1,1000) == 42):
            #             child = self.mutate(child)


            #     childTreeA = childrenTrees[0]
            #     childTreeB = childrenTrees[1]
                
                
            #     if (childTreeA.findFitness(data) <= childTreeB.findFitness(data) ):
            #         newPopulation.append(childTreeA)
            #     else:
            #         newPopulation.append(childTreeB)

    

        # finalFitness = []

        # for tree in population:
        #     finalFitness.append((tree, tree.findFitness(data)))

        # # print(len(finalPopulation))

        return min(population, key = lambda t: t.fitness)




def main():

    data = pd.read_csv('dataset1.csv')

    # print(len(data))
    trainingSet, testSet = train_test_split(data, test_size=0.2)
    

    player = GeneticProgramming(100)

    # trainingArray = np.array()
    # testArray = np.array()

    

    # for index, row in trainingSet.iterrows():
    #     trainingArray.append((row['x'],row['f(x)']))
    trainingArray = trainingSet.values

    # trainingArray = [[16.16],[16,16]]
    testArray = testSet.values

    # data = []

    # for i in range(20):
    #     data.append((.66, 18))

    
    winner = player.symbReg(200, 30, trainingArray)

    print (winner.toString())
    print(winner.fitness)

    print("Test Set")
    print(winner.findFitness(testArray))

    tree = ExpressionTree.ExpressionTree(testArray)
    print(tree.toString())
    

    
    # print (data.loc[0]["x"])

    # population = []

    # for i in range (100):
    #     tree = ExpressionTree.ExpressionTree(trainingArray)

    #     population.append(tree)

        # print (tree.findFitness(trainingArray))

    # tree = ExpressionTree.ExpressionTree(trainingArray)
    # treeb = ExpressionTree.ExpressionTree(trainingArray)
    # print(tree.toString())

    # setty = player.crossOver(tree, treeb,trainingArray)

    # print(tree.fitness)
    # print(setty[0].fitness)

    # print(treeb.fitness)
    # print(setty[1].fitness)



    # print (player.tournamentSelection(population))
    # tree.findFitness(data)


    





if __name__ == "__main__":
    main()


        




    


        