import ExpressionTree
import random


class ExpressionTree:

    def __init__(self, numGen):
        self.numGen = numGen
        
    def crossOver(self, treeA, treeB):
        depthA = treeA.findDepth()
        depthB = treeB.findDepth()

        crossDepthA = random.randint(1, depthA)
        crossDepthB = random.randint(1, depthB)


    


        