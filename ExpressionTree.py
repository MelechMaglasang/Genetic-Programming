import Node

class ExpressionTree:
    def __init__(self, root):

        self.root = root

    def PrintTree(self):
        self.root.PrintTree()

def main():
    node = Node.Node("*")

    nodeRight = Node.Node("+")

    nodeChildRight = Node.Node("2")

    nodeChildRight2 = Node.Node("5")

    nodeLeft = Node.Node("125")

    node.insertRight(nodeRight)

    node.insertLeft(nodeLeft)

    nodeRight.insertRight(nodeChildRight)

    nodeRight.insertLeft(nodeChildRight2)

    tree = ExpressionTree(node)
    tree.PrintTree()



if __name__ == "__main__":
    main()
