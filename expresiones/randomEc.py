from expresiones import *
from randomExpr import *
import random

# Este metodo recibe el numero de terminos y una lista con las operaciones a utilizar.
# Retorna un diccionario con dos vectores, uno que contiene a las fracciones que componen
# la expresion y otro que contiene las operaciones a realizar.
def randomEcuation(n, operations, numRange, denRange, neg, auto_reduc):
    oper = []
    fracs = []
    for i in range(n-1):
        oper += [randOp(operations)]
        fracs += [randFrac(numRange, denRange, neg, auto_reduc)]
    fracs += [randFrac(numRange, denRange, neg, auto_reduc)]
    return {"operations":oper, "elements":fracs}

def solveStepEcuation(dict):
    operations = dict["operations"]
    elements = dict["elements"]
    solved = False
    index = 0

    while(not solved and index < len(operations)):
        if operations[index] == "*":
            newElement = mulFrac(elements[index], elements[index+1])
            solved = True
            index -= 1
        elif operations[index] == ":":
            newElement = divFrac(elements[index], elements[index+1])
            solved = True
            index -= 1
        index += 1

    if not solved:
        index = 0
        if operations[0] == "+":
            newElement = sumFrac(elements[0], elements[1])
        elif operations[0] == "-":
            newElement = subFrac(elements[0], elements[1])

    operations.pop(index)
    elements.pop(index)
    elements.pop(index)
    elements.insert(index, newElement)
    return {"operations":operations, "elements":elements}

def ecToString(dict):
    operations = dict["operations"]
    elements = dict["elements"]
    chain = ''
    for i in range(len(operations)):
        chain += elements[i].getStr()
        chain += ' '
        chain += operations[i]
        chain += ' '
    chain += elements[-1].getStr()
    return chain

def solveEcuation(expretion):
    while(len(expretion["elements"]) > 1):
        print(ecToString(expretion))
        expretion = solveStepEcuation(expretion)
    print(expretion["elements"][0].getStr())

def solveEcuation_toString(expretion):
    results = []
    while(len(expretion["elements"]) > 1):
        results += [ecToString(expretion)]
        expretion = solveStepEcuation(expretion)
    results += [expretion["elements"][0].getStr()]
    return results