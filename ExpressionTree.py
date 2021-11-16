import Node
import random
import io
import sys
import copy

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


class ExpressionTree:

    # operands = {"+", "-", "/", "*", "**"}
    operands = {"+", "-", "*"}
    # Discussion about multiply and divide being basically the same thing so we cacn add the zero if we get rid of divide
    #leafVals = {"-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3","4", "5"}
    leafVals = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    def __init__(self, data):
        # Depth cite that paper later
        depth = random.randint(1, 10)
        self.root = Node.Node()

        curr = self.root

        self.treeBrancher(curr, depth, depth)

        self.nodeFiller(curr)
        # self.expression = self.toString()

        self.fitness = self.findFitness(data)

    def findDepth(self):
        return self.root.findDepth(self.root)

    # recursive branch creator the node inserted will have children possibly
    def treeBrancher(self, node, depth, maxDepth):
        # node.depth = maxDepth - depth + 1
        if (depth == 0):
            return depth

        if (random.randint(1, 3) != 1):
            newNode = Node.Node()
            node.rightChild = newNode
            self.treeBrancher(node.rightChild, depth - 1, maxDepth)

            newNodeLeft = Node.Node()
            node.leftChild = newNodeLeft
            self.treeBrancher(node.leftChild, depth - 1, maxDepth)
        # else:

            # This may be for unary operators

            # if (random.randint(1,2) == 1000):
            #     newNode = Node.Node()
            #     node.rightChild = newNode
            #     self.treeBrancher(node.rightChild, depth -1)

            # else:

    def grabNodesAtDepth(self, depth):
        array = []

        self.grabNodesHelper(1, depth, self.root, array)

        return array

    def grabNodesHelper(self, currDepth, depth, node, array):

        if(node == None or currDepth > depth):
            return
        elif (currDepth == depth and node.rightChild != None and node.leftChild != None):
            # print(currDepth, node.depth)
            array.append(node)
            return

        else:
            self.grabNodesHelper(currDepth+1, depth, node.leftChild, array)
            self.grabNodesHelper(currDepth+1, depth, node.rightChild, array)

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

    # # Possibly naive implementation
    # def expSolver(self, val):
    #     exp = self.expression.replace("x", str(val))

    #     # We Need to catch divisions by zero, I took out the zero as of now
    #     try:
    #         result = eval(exp)

    #     except ZeroDivisionError:
    #         return sys.maxsize

    #     return result

    def evaluateExpressionTree(self, root, val):

        # empty tree
        if root is None:
            return 0

        # leaf node
        if root.leftChild is None and root.rightChild is None:
            if (root.nodeValue == 'x'):
                return val
            else:
                return int(root.nodeValue)

        # evaluate left tree
        leftSum = self.evaluateExpressionTree(root.leftChild, val)

        # evaluate right tree
        rightSum = self.evaluateExpressionTree(root.rightChild, val)

        # check which operation to apply
        if root.nodeValue == '+':
            return leftSum + rightSum

        elif root.nodeValue == '-':
            return leftSum - rightSum

        elif root.nodeValue == '*':
            return leftSum * rightSum

        else:
            if rightSum == 0:
                return 1
            else:
                return leftSum / rightSum

    # These print an in order traversal of the possible expression

    def findFitness(self, data):
        y_true = []
        y_pred = []
        for i in range(len(data)):
            y_pred.append(self.evaluateExpressionTree(self.root, data[i][0]))
            y_true.append(data[i][1])
          
        return mean_squared_error(y_true, y_pred)

    def PrintTree(self):
        self.root.PrintTree()
        print()

    def stringHelper(self, output, root):
        if (root.leftChild == None and root.rightChild == None):
            output.write(root.nodeValue)
        else:
            output.write("(")
            self.stringHelper(output, root.leftChild)
            output.write(root.nodeValue)
            self.stringHelper(output, root.rightChild)
            output.write(")")


    def toString(self):

        output = io.StringIO()
        
        self.stringHelper(output, self.root)

        contents = output.getvalue()

        output.close()

        return contents


def main():

    tree = ExpressionTree()

    tree.PrintTree()
    print()
    # print(tree.expSolver(0.5))

    print(tree.grabNodesAtDepth(2))

    population = []

    for i in range(100):
        tree = ExpressionTree()

        population.append(tree)

    for tree in population:
        print(tree.evaluateExpressionTree(tree.root, .5))

        # print (tree.expression)

if __name__ == "__main__":
    main()
