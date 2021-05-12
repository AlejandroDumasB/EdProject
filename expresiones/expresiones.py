# Clase que representa una expresion matematica, compuesta por la operacion entre 2 sub-expresiones
# expr1 : Expresion, Int, Fraccion
# op    : simbolo (+, -, *, /)
# expr2 : Expresion, Int, Fraccion
class Expresion:

    def __init__(self, expr1, op, expr2):
        self.operacion = op
        self.expr1 = expr1
        self.expr2 = expr2

# Metodo que recibe una Expresion de enteros y la resuelve, retornando un entero.
def resolver(expr):
    if (isinstance(expr, int)):
        return expr
    elif expr.operacion == '+':
        return resolver(expr.expr1) + resolver(expr.expr2)
    elif expr.operacion == '-':
        return resolver(expr.expr1) - resolver(expr.expr2)
    elif expr.operacion == '*':
        return resolver(expr.expr1) * resolver(expr.expr2)
    elif expr.operacion == ':':
        return resolver(expr.expr1) / resolver(expr.expr2)

# Metodo Auxiliar que utiliza la funcion imprimir()
def imprimirAux(expr):
    if (isinstance(expr, int)):
        print(expr, end='')
    elif (isinstance(expr, Fraccion)):
        expr.print()
    else:
        print('(', end='')
        imprimirAux(expr.expr1)
        print(' ' + expr.operacion + ' ', end='')
        imprimirAux(expr.expr2)
        print(')', end='')

# Metodo que recibe una Expresion y la imprime en pantalla
def imprimir(expr):
    if (isinstance(expr, int)):
        print(expr)
    elif (isinstance(expr, Fraccion)):
        expr.print()
        #print('')
    else:
        imprimirAux(expr.expr1)
        print(' ' + expr.operacion + ' ', end='')
        imprimirAux(expr.expr2)
        print('')

# Metodo auxiliar que utiliza la funcion imprimir_toStr()
def imprimir_toStr_Aux(expr):
    result = ''
    if (isinstance(expr, int)):
        result = str(expr)
    elif (isinstance(expr, Fraccion)):
        result = expr.getStr()
    else:
        result = '('
        result += imprimir_toStr_Aux(expr.expr1)
        result += (' ' + expr.operacion + ' ')
        result += imprimir_toStr_Aux(expr.expr2)
        result += ')'
    return result

# Metodo que recibe una Expresion y retorna un String que la representa
def imprimir_toStr(expr):
    result = ''
    if (isinstance(expr, int)):
        result = str(expr)
    elif (isinstance(expr, Fraccion)):
        result = expr.getStr()
    else:
        result += imprimir_toStr_Aux(expr.expr1)
        result += (' ' + expr.operacion + ' ')
        result += imprimir_toStr_Aux(expr.expr2)
    return result

# Metodo que calcula el Maximo Comun Divisor entre dos enteros
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

# Clase que representa una fraccion matematica
# numerador   : Int
# denominador : Int
# auto_reduc  : Bool
class Fraccion:

    def __init__(self, numerador, denominador, auto_reduc=True):
        self.num = numerador
        self.den = denominador
        self.auto_reduc = auto_reduc

    def sum(self, fraccion):
        self.num = (self.num * fraccion.den) + (self.den * fraccion.num)
        self.den *= fraccion.den

    def sub(self, fraccion):
        self.num = (self.num * fraccion.den) - (self.den * fraccion.num)
        self.den *= fraccion.den

    def mul(self, fraccion):
        self.num *= fraccion.num
        self.den *= fraccion.den

    def div(self, fraccion):
        self.num *= fraccion.den
        self.den *= fraccion.num
    
    # Metodo que reduce la fraccion segun el maximo comun divisor entre
    # su denominador y su numerador
    def reduc(self):
        div = mcd(self.num, self.den)
        if div != 1:
            self.num //= div
            self.den //= div

    # Metodo que imprime en pantalla la Fraccion
    def print(self):
        if self.auto_reduc:
            self.reduc()
        if self.num == 0:
            print('0', end = '')
        elif self.den == 1:
            print(self.num, end='')
        else:
            print('{0}/{1}'.format(self.num, self.den), end='')
    
    # Metodo que retorna un String que representa a la Fraccion    
    def getStr(self):
        if self.auto_reduc:
            self.reduc()
        if self.num == 0:
            result = '0'
        elif self.den == 1:
            result = str(self.num)
        else:
            result = '{0}/{1}'.format(self.num, self.den)
        return result

# Metodo que recibe dos Fracciones y retorna una Fraccion que representa su suma
def sumFrac(f1, f2):
    num = (f1.num * f2.den) + (f1.den * f2.num)
    den = f1.den * f2.den
    return Fraccion(num, den)

# Metodo que recibe dos Fracciones y retorna una Fraccion que representa su resta
def subFrac(f1, f2):
    num = (f1.num * f2.den) - (f1.den * f2.num)
    den = f1.den * f2.den
    return Fraccion(num, den)

# Metodo que recibe dos Fracciones y retorna una Fraccion que representa su multiplicacion
def mulFrac(f1, f2):
    num = f1.num * f2.num
    den = f1.den * f2.den
    return Fraccion(num, den)

# Metodo que recibe dos Fracciones y retorna una Fraccion que representa su division
def divFrac(f1, f2):
    num = f1.num * f2.den
    den = f1.den * f2.num
    return Fraccion(num, den)

# Metodo que recibe una Expresion de Fracciones/Enteros y la resuelve, retornando una Fraccion.
def resolverFrac(expr):
    if (isinstance(expr, Fraccion)):
        return expr
    elif (isinstance(expr, int)):
        return Fraccion(expr, 1)
    elif expr.operacion == '+':
        return sumFrac(resolverFrac(expr.expr1), resolverFrac(expr.expr2))
    elif expr.operacion == '-':
        return subFrac(resolverFrac(expr.expr1), resolverFrac(expr.expr2))
    elif expr.operacion == '*':
        return mulFrac(resolverFrac(expr.expr1), resolverFrac(expr.expr2))
    elif expr.operacion == ':':
        return divFrac(resolverFrac(expr.expr1), resolverFrac(expr.expr2))

# Metodo que recibe una Expresion de Fracciones/Enteros, y siguiento las reglas presentadas
# por los parentesis de la expresion, resuelve solo una de las operaciones. Siempre resuelve
# la operacion mas interna, y a la izquierda 
def resolverStepFrac(expr):
    if (isinstance(expr.expr1, Fraccion)) and (isinstance(expr.expr2, Fraccion)):
        if expr.operacion == '+':
            return sumFrac(expr.expr1, expr.expr2)
        elif expr.operacion == '-':
            return subFrac(expr.expr1, expr.expr2)
        elif expr.operacion == '*':
            return mulFrac(expr.expr1, expr.expr2)
        elif expr.operacion == ':':
            return divFrac(expr.expr1, expr.expr2)
    else:
        if (isinstance(expr.expr1, Fraccion)):
            return Expresion(expr.expr1, expr.operacion, resolverStepFrac(expr.expr2))
        else:
            return Expresion(resolverStepFrac(expr.expr1), expr.operacion, expr.expr2)

# Metodo que recibe una expresion, y la resulve paso a paso, imprimiendo en pantalla cada uno
# expr : Expresion (Fraccion/Int)
def resolverSteps(expr):
    imprimir(expr)
    while not isinstance(expr.expr1, Fraccion) or not isinstance(expr.expr2, Fraccion):
        expr = resolverStepFrac(expr)
        imprimir(expr)
    f = resolverFrac(expr)
    f.print()
    print('')

# Metodo que recibe una expresion, y la resulve paso a paso, retornando una lista con los Strings
# correspondientes a cada paso de la resolucion
# expr : Expresion (Fraccion/Int)
def resolverSteps_toString(expr):
    results = []
    results += [imprimir_toStr(expr)]
    while not isinstance(expr.expr1, Fraccion) or not isinstance(expr.expr2, Fraccion):
        expr = resolverStepFrac(expr)
        results += [imprimir_toStr(expr)]
    f = resolverFrac(expr)
    results += [f.getStr()]
    return results

# Metodo que recibe un string que representa una expresion matematica y los transforma
# al formato utilizado en Open Office
def openOfficeFormat(chain):
    newChain = ''
    aux = False
    for char in chain:
        if char == '(':
            newChain += 'left( '
        elif char == ')':
            if aux:
                newChain += ' }'
                aux = False
            newChain += ' right)'
        elif char == '*':
            newChain += 'ddot'
        elif char == '/':
            newChain += ' over '
        elif char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and not aux:
            newChain += ('{ ' + char)
            aux = True
        elif char == ' ' and aux:
            newChain += ' } '
            aux = False
        else:
            newChain += char
    if chain[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        newChain += ' }'
    return newChain