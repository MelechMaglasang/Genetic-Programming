import ExpressionTree
import Node
import random
import copy


class GeneticProgramming:

    def __init__(self, numGen):
        self.numGen = numGen
        
    def crossOver(self, treeA, treeB):
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

        if (newTreeA.root == None or newTreeB.root == None):
            print ("whoa")

        newTreeA.expression = newTreeA.toString()
        newTreeB.expression = newTreeB.toString()
            
        return (newTreeA, newTreeB)


    def mutate(self, tree):
        depth = tree.findDepth()

        newTree = copy.deepcopy(tree)

        mutagen = Node.Node()
        leftLeaf = Node.Node()
        rightLeaf = Node.Node()

        mutagen.leftChild = leftLeaf
        mutagen.rightChild = rightLeaf

        mutagen.nodeValue = random.sample(mutagen.operands, 1)[0] 

        if (random.randint(1, 3) == 1):
            leftLeaf.nodeValue = "x"
        else:
            leftLeaf.nodeValue = random.sample(leftLeaf.leafVals, 1)[0]

        if (random.randint(1, 3) == 1):
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
            

        return newTree



        




        

        




            


        


def main():
    treeA = ExpressionTree.ExpressionTree()

    # print(treeA.toString())

    treeB = ExpressionTree.ExpressionTree()

    player = GeneticProgramming(10)

    # print (newTree.toString())



    setty = player.crossOver(treeA, treeB)

    print(treeA.toString())
    print(setty[0].toString())



    print(treeB.toString())
    print(setty[1].toString())

    gen2A =setty[0]
    gen2B = setty[1]

    setty2 = player.crossOver(gen2A, gen2B)

    print(gen2A.toString())
    print(setty2[0].toString())



    print(gen2B.toString())
    print(setty2[1].toString())

    mutatedTree = player.mutate(setty2[1])

    print(mutatedTree.toString())



if __name__ == "__main__":
    main()


        




    


        