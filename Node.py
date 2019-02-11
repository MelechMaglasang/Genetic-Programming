class Node:

    operands = {"+","-","/","*"}

    def __init__(self, nodeValue):

        self.leftChild = None
        self.rightChild = None
        self.nodeValue = nodeValue

    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.nodeValue , end='')

        if self.rightChild:
            self.rightChild.PrintTree()


    def isOperand(self):
        return (self.nodeValue in self.operands)


    def insertRight(self, node):
        if self.rightChild == None:
            self.rightChild = node
            return True
        else:
            return False 
    def insertLeft(self, node):
        if self.leftChild == None:
            self.leftChild = node
            return True
        else:
            return False
        


def main():
    node = Node("*")

    nodeRight = Node("+")

    nodeChildRight = Node("2")

    nodeChildRight2 = Node("5")

    nodeLeft = Node("125")

    node.insertRight(nodeRight)

    node.insertLeft(nodeLeft)

    nodeRight.insertRight(nodeChildRight)

    nodeRight.insertLeft(nodeChildRight2)
    node.PrintTree()



if __name__ == "__main__":
    main()
