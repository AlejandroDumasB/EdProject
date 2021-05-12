# Proyecto Jose/Cio

Jefe: Jose Rodriguez

Codigo: Alejandro Dumas, Rocio Campos
        
# Expresiones

Las funciones de randExprFrac() y randomEcuation() crean los objetos que representan a una expresion.
Luego, se deben utilizar las funciones resolverSteps_toString() y solveEcuation_toString() respectivamente
para poder resolver el problema. Estas ultimos metodos retornan una lista de Strings, en donde cada uno
representa un paso en la reduccion del problema original.
 
Forma de uso:

expr = randExprFrac(...)
steps = resolverSteps_toString(expr)

expr = randomEcuation(...)
steps = solveEcuation_toString(expr)

En ambos casos, steps[0] contendra a la expresion original y steps[-1] contendra el resultado final
