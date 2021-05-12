from expresiones import *
import random

# Funcion que retorna un operador aleatoriamente (+, -, * o /)
def randOp(operations):
    return random.choice(operations)

# Funcion que recibe el numero de terminos y retorna un objeto Expresion aleatorio del tamaño pedido
# n -> Define el numero de terminos que componen la expresion
def randExpr(n, operations):
    if n == 1:
        num = random.randint(-50, 50)
        if num == 0:
            return random.randint(1, 50)
        else:
            return num
    else:
        op = randOp(operations)
        div = random.random()
        a = round(div*n)
        b = n-a
        if a == 0 and b > 1:
            return Expresion(randExpr(1, operations), op, randExpr(b-1, operations))
        elif b == 0 and a > 1:
            return Expresion(randExpr(a-1, operations), op, randExpr(1, operations))
        else:
            return Expresion(randExpr(a, operations), op, randExpr(b, operations))

# Fucion que retorna un objeto Fraccion aleatorio
# numRange (opcional)-> Define el rango del numerador (1 hasta numRange)
# denRange (opcional)-> Define el rango del denominador (1 hasta denRange)
# neg (opcional) -> Un valor booleano que define si al expresion puede ser negativa o no
#                   neg=False implica que el metodo solo puede retornar fracciones positivas
#                   neg=True implica que el metodo puede retornar fracciones positivas o negativas
def randFrac(numRange=20, denRange=20, neg=False, auto_reduc=True):
    numerador = random.randint(1, numRange)
    if neg:
        numerador = random.randint(numRange-2*numRange, numRange)
    denominador = random.randint(1, denRange)
    return Fraccion(numerador, denominador, auto_reduc=auto_reduc)

#Funcion que recibe el numero de terminos y retorna un objeto Expresion aleatorio, compuesto de Fracciones
# n -> Define el numero de terminos que componen la expresion
def randExprFrac(n, operations, numRange, denRange, neg, auto_reduc):
    if n == 1:
        return randFrac(numRange, denRange, neg, auto_reduc)
    else:
        op = randOp(operations)
        div = random.random()
        a = round(div*n)
        b = n-a
        if a == 0 and b > 1:
            return Expresion(randExprFrac(1, operations, numRange, denRange, neg, auto_reduc), op, randExprFrac(b-1, operations, numRange, denRange, neg, auto_reduc))
        elif b == 0 and a > 1:
            return Expresion(randExprFrac(a-1, operations, numRange, denRange, neg, auto_reduc), op, randExprFrac(1, operations, numRange, denRange, neg, auto_reduc))
        else:
            return Expresion(randExprFrac(a, operations, numRange, denRange, neg, auto_reduc), op, randExprFrac(b, operations, numRange, denRange, neg, auto_reduc))