from randomExpr import *
from expresiones import *
from randomEc import *

# Variables Globales
NUMERADOR_RANGO = 9
DENOMINADOR_RANGO = 9
NEGATIVOS = False
AUTO_REDUCCION = True
OPERACIONES = ['+', '-', '*', ':']
FORMATO_OPEN_OFFICE = False
PARENTESIS = False

n_ejercicios = int(input('Ingresar el numero de ejercicios que desea: '))
while n_ejercicios < 1:
    n_ejercicios = int(input('Numero de ejercicios debe ser mayor que 0, intente de nuevo: '))
n_terminos = int(input('Ingresar el numero de terminos de cada ejercicio: '))
while n_terminos < 2:
    n_terminos = int(input('Numero de terminos debe ser mayor que 1, intente de nuevo: '))


# Las funciones de randExprFrac() y randomEcuation() crean los objetos que representan a una expresion.
# Luego, se deben utilizar las funciones resolverSteps_toString() y solveEcuation_toString() respectivamente
# para poder resolver el problema. Estas ultimos metodos retornan una lista de Strings, en donde cada uno
# representa un paso en la reduccion del problema original.
# 
# Forma de uso:
#
# expr = randExprFrac(...)
# steps = resolverSteps_toString(expr)
#
# expr = randomEcuation(...)
# steps = solveEcuation_toString(expr)
#
# En ambos casos, steps[0] contendra a la expresion original y steps[-1] contendra el resultado final

print('')
for i in range(n_ejercicios):
    if PARENTESIS:
        expr = randExprFrac(n_terminos, OPERACIONES, NUMERADOR_RANGO, DENOMINADOR_RANGO, NEGATIVOS, AUTO_REDUCCION)
        steps = resolverSteps_toString(expr)
    else:
        expr = randomEcuation(n_terminos, OPERACIONES, NUMERADOR_RANGO, DENOMINADOR_RANGO, NEGATIVOS, AUTO_REDUCCION)
        steps = solveEcuation_toString(expr)
    print('Ejercicio {0}'.format(i+1))
    for step in steps:
        if FORMATO_OPEN_OFFICE:
            step = openOfficeFormat(step)
        print(step)
    print('')