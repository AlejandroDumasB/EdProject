import random
from expresiones import *
from randomExpr import *

class ExprNode:

    def __init__(self, value, nodeIzq=None, nodeDer=None):
        if isinstance(value, str):
            self.op = value
            self.num = None
            self.left = nodeIzq
            self.right = nodeDer
        else:
            self.op = None
            self.num = value
            self.left = nodeIzq
            self.right = nodeDer
    
def randExprTree(n):
    if n == 1:
        return ExprNode(random.randint(1, 50))
    else:
        op = randOp()
        div = random.random()
        a = round(div*n)
        b = n-a
        if a == 0 and b > 1:
            return ExprNode(op, randExprTree(1), randExprTree(b-1))
        elif b == 0 and a > 1:
            return ExprNode(op, randExprTree(a-1), randExprTree(1))
        else:
            return ExprNode(op, randExprTree(a), randExprTree(b))

def printTree(tree):
    if tree.op == None:
        print(tree.num, end='')
    else:
        print('(', end='')
        printTree(tree.left)
        print(' ' + tree.op + ' ', end='')
        printTree(tree.right)
        print(')', end='')

expr = randExprTree(5)
printTree(expr)