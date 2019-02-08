class Node:

    def __init__(self, nodeValue):

        self.leftChild = None
        self.rightChild = None
        self.nodeValue = nodeValue


    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.nodeValue)
        if self.rightChild:
            self.rightChild.PrintTree()


def main():
    node = Node(100)

    nodeRight = Node(12)

    node.rightChild = nodeRight

    node.PrintTree()



if __name__ == "__main__":
    main()
