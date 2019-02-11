import Node
import random

class ExpressionTree:

    operands = {"+","-","/","*"}
    leafVals = {"1","2","3", "4", "5", "6", "7", "8", "9", "0"}

    
    def __init__(self):

        depth = random.randint(2,4)
        self.root = Node.Node("&")

        curr = self.root

        self.treeBrancher(curr, depth)

        self.nodeFiller(curr)

    #recursive branch creator the node inserted will have children possibly 
    def treeBrancher(self, node, depth):
        if (depth == 0):
            return depth
        else:

            #This may be for unary operators 

            # if (random.randint(1,2) == 1000):
            #     newNode = Node.Node("&")
            #     node.rightChild = newNode
            #     self.treeBrancher(node.rightChild, depth -1)

            # else:
                
            newNode = Node.Node("&")
            node.rightChild = newNode
            self.treeBrancher(node.rightChild, depth -1)

            newNodeLeft = Node.Node("&")
            node.leftChild = newNodeLeft
            self.treeBrancher(node.leftChild, depth -1)

    def nodeFiller(self,node):
        if node.leftChild:
            self.nodeFiller(node.leftChild)
        # print(self.nodeValue)

        #If its a leaf
        if (node.rightChild == None and node.leftChild == None):
            if (random.randint(1,2) == 1):
                node.nodeValue = random.sample(ExpressionTree.leafVals,1)[0]
            else:
                node.nodeValue = "x"
        else:
            node.nodeValue = random.sample(ExpressionTree.operands,1)[0]

        if node.rightChild:
            self.nodeFiller(node.rightChild)
            
    def PrintTree(self):
        self.root.PrintTree()



def main():

    tree = ExpressionTree()

    tree.PrintTree()

    # temp = "9"


    # node = Node.Node("*")
    
    # nodeRight = Node.Node("+")

    # nodeChildRight = Node.Node("2")

    # nodeChildRight2 = Node.Node("5")

    # nodeLeft = Node.Node("125")

    # node.insertRight(nodeRight)

    # node.insertLeft(nodeLeft)

    # nodeRight.insertRight(nodeChildRight)

    # nodeRight.insertLeft(nodeChildRight2)

    # tree = ExpressionTree(node)


    # tree.PrintTree()

    # # print (temp in tree.operands)
    # print(node.isOperand())

    # print(nodeChildRight2.isOperand())



if __name__ == "__main__":
    main()
