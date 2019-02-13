import Node
import random
import io
import sys


class ExpressionTree:

    operands = {"+", "-", "/", "*"}
    #Discussion about multiply and divide being basically the same thing so we cacn add the zero if we get rid of divide
    leafVals = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    def __init__(self):
        #Depth cite that paper later
        depth = random.randint(1, 17)
        self.root = Node.Node("&")

        curr = self.root

        self.treeBrancher(curr, depth)

        self.nodeFiller(curr)

        self.expression = self.toString()

    # recursive branch creator the node inserted will have children possibly
    def treeBrancher(self, node, depth):
        if (depth == 0):
            return depth

        if (random.randint(1, 2) == 1):
            newNode = Node.Node("&")
            node.rightChild = newNode
            self.treeBrancher(node.rightChild, depth - 1)

            newNodeLeft = Node.Node("&")
            node.leftChild = newNodeLeft
            self.treeBrancher(node.leftChild, depth - 1)
        # else:

            # This may be for unary operators

            # if (random.randint(1,2) == 1000):
            #     newNode = Node.Node("&")
            #     node.rightChild = newNode
            #     self.treeBrancher(node.rightChild, depth -1)

            # else:

          

    def nodeFiller(self, node):
        if node.leftChild:
            self.nodeFiller(node.leftChild)
        # print(self.nodeValue)

        # If its a leaf
        if (node.rightChild == None and node.leftChild == None):
            if (random.randint(1, 3) == 1):
                node.nodeValue = "x"
            else:
                node.nodeValue = random.sample(ExpressionTree.leafVals, 1)[0]

                
        else:
            node.nodeValue = random.sample(ExpressionTree.operands, 1)[0]

        if node.rightChild:
            self.nodeFiller(node.rightChild)

    # Possibly naive implementation
    def expSolver(self, val):
        exp = self.expression.replace("x", str(val))

        # We Need to catch divisions by zero, I took out the zero as of now
        try:
            result = eval(exp)

        except ZeroDivisionError:
            return sys.maxsize

        return result

    # These print an in order traversal of the possible expression
    def PrintTree(self):
        self.root.PrintTree()

    def stringHelper(self, output, node):
        if node.leftChild:
            self.stringHelper(output, node.leftChild)
        # print(node.nodeValue , end='')
        output.write(node.nodeValue)

        if node.rightChild:
            # node.rightChild.PrintTree()
            self.stringHelper(output, node.rightChild)

    def toString(self):

        output = io.StringIO()

        # self.root.PrintTree()
        self.stringHelper(output, self.root)

        contents = output.getvalue()

        output.close()

        return contents


def main():

    for i in range(100):
        tree = ExpressionTree()

        tree.PrintTree()
        print()
        print(tree.expSolver(5))

        # print (tree.expression)

    # temp = "9"

    # string = "x*x/4-1*2+3/6-4*x/x-9*1+x+x*x*5"

    # print (string.replace('x', '69'))

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
