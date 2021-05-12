from turtle import *

# Parametros Globales

# Colores
color_lineas = "black"
color_base = "white"
color_achurado = "blue"
color_background = "white"

# Dimension ventana
largo_img = 900
alto_img = 500

# Dimensiones representacion fraccion
ancho_lineas = 5
largo = 200
alto = 200
x0 = -100
y0 = 100

s = getscreen()
s.screensize(largo_img, alto_img)
s.bgcolor(color_background)
pensize(ancho_lineas)
ht()
speed(0)

def dibujar_linea(x0, y0, largo, mode):
    penup()
    goto(x0, y0)
    pendown()
    if (mode == "h"):
        fd(largo)
    elif (mode == "v"):
        rt(90)
        fd(largo)
        lt(90)

def dibujar_rectangulo(x0, y0, largo, alto):
    penup()
    goto(x0, y0)
    pendown()
    fd(largo)
    rt(90)
    fd(alto)
    rt(90)
    fd(largo)
    rt(90)
    fd(alto)
    rt(90)

def dibujar_mas(x, y):
    penup()
    goto(x-25, y)
    pendown()
    fd(50)
    penup()
    goto(x, y+25)
    pendown()
    rt(90)
    fd(50)
    lt(90)

def dibujar_igual(x, y):
    penup()
    goto(x-25, y+15)
    pendown()
    fd(50)
    penup()
    goto(x-25, y-15)
    pendown()
    fd(50)

#########################################################################################
################################## DIBUJAR_FRACCION #####################################
#########################################################################################
#
# numerador -> numerador de la fraccion representada
#
# denominador -> denominador de la fraccion representada
#
# mode -> define la orientacion de la fraccion ("h" para horizontal y "v" para vertical)
#
# x0 (opcional) -> define la coordenada x de la ezquina superior izquierda del dibujo
#
# y0 (opcional) -> define la coordenada y de la ezquina superior izquierda del dibujo
#
# largo (opcional) -> define el largo (eje x) de la representacion
#
# alto (opcional) -> define el alto (eje y) de la representacion
#
# color_achurado (opcional) -> define el color de la region achurada de la fraccion
#
# color_base (opcional) -> define el color de la region no achurada de la fraccion
#
# color_lineas (opcional) -> define el color de las lineas de la representacion
#
# color_background (opcional) -> define el color del fondo de la ventana de visualizacion
#
############################################################################################
############################################################################################
def dibujar_fraccion(numerador, denominador, mode, inter=0, x0=x0, y0=y0, largo=largo, alto=alto, 
                    color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                    color_background=color_background):
    s.bgcolor(color_background)

    if (numerador < 0 or denominador <= 0):
        print("Error: El numerador es negativo o el denominador es <= 0")
        exit()
        return

    elif (numerador <= denominador):
        x = x0
        y = y0
        if (mode == "v"):
            delta_x = largo/denominador
            color(color_lineas, color_achurado)
            for i in range(numerador):
                begin_fill()
                dibujar_rectangulo(x, y, delta_x, alto)
                end_fill()
                x = x + delta_x
            color(color_lineas, color_base)
            for i in range(denominador-numerador):
                begin_fill()
                dibujar_rectangulo(x, y, delta_x, alto)
                end_fill()
                x = x + delta_x
        elif (mode == "h"):
            delta_y = alto/denominador
            color(color_lineas, color_achurado)
            for i in range(numerador):
                begin_fill()
                dibujar_rectangulo(x, y, largo, delta_y)
                end_fill()
                y = y - delta_y
            color(color_lineas, color_base)
            for i in range(denominador-numerador):
                begin_fill()
                dibujar_rectangulo(x, y, largo, delta_y)
                end_fill()
                y = y - delta_y

        if (inter != 0):
            if (mode == "v"):
                delta = alto/inter
                for i in range(inter-1):
                    dibujar_linea(x0, y0 - delta*(i+1), largo, "h")
            elif (mode == "h"):
                delta = largo/inter
                for i in range(inter-1):
                    dibujar_linea(x0 + delta*(i+1), y0, alto, "v")
        
    elif (numerador <= 2*denominador):
        x = x0
        y = alto + 10
        dibujar_fraccion(denominador, denominador, mode, inter, x0=x, y0=y, largo=largo, alto=alto, 
                        color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                        color_background=color_background)
        y = -10
        dibujar_fraccion((numerador - denominador), denominador, mode, inter, x0=x, y0=y, largo=largo, alto=alto, 
                        color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                        color_background=color_background)
    
    else:
        print("Error: La fraccion a representar tiene un valor mayor que 2")
        exit()
        return



#########################################################################################
############################### DIBUJAR_SUMA_FRACCIONES #################################
#########################################################################################
#
# num1 -> numerador de la 1era fraccion representada
#
# den1 -> denominador de la 1era fraccion representada
#
# num2 -> numerador de la 2da fraccion representada
#
# den2 -> denominador de la 2da fraccion representada
#
# x0 (opcional) -> define la coordenada x de la ezquina superior izquierda del dibujo
#
# y0 (opcional) -> define la coordenada y de la ezquina superior izquierda del dibujo
#
# largo (opcional) -> define el largo (eje x) de la representacion
#
# alto (opcional) -> define el alto (eje y) de la representacion
#
# color_achurado (opcional) -> define el color de la region achurada de la fraccion
#
# color_base (opcional) -> define el color de la region no achurada de la fraccion
#
# color_lineas (opcional) -> define el color de las lineas de la representacion
#
# color_background (opcional) -> define el color del fondo de la ventana de visualizacion
#
############################################################################################
############################################################################################
def dibujar_suma_fracciones(num1, den1, num2, den2, x0=x0, y0=y0, largo=largo, alto=alto, 
                        color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                        color_background=color_background):
    s.bgcolor(color_background)
    numero_achurados = num1*den2 + num2*den1
    numero_total = den1*den2

    if (numero_achurados < 0 or numero_total <= 0):
        print("Error: El numerador es negativo o el denominador es <= 0")
        exit()
        return

    elif (numero_achurados <= numero_total):
        x = x0
        y = y0
        delta_x = largo/den2
        delta_y = alto/den1
        color(color_lineas, color_achurado)
        for i in range(numero_achurados):
            begin_fill()
            dibujar_rectangulo(x, y, delta_x, delta_y)
            end_fill()
            if (x >= x0 + (delta_x*(den2 - 1)) - ancho_lineas):
                x = x0
                y = y - delta_y
            else:
                x = x + delta_x
        color(color_lineas, color_base)
        for i in range(numero_total - numero_achurados):
            begin_fill()
            dibujar_rectangulo(x, y, delta_x, delta_y)
            end_fill()
            if (x >= x0 + (delta_x*(den2 - 1)) - ancho_lineas):
                x = x0
                y = y - delta_y
            else:
                x = x + delta_x

    elif (numero_achurados <= 2*numero_total):
        x = x0
        y = alto + 10
        dibujar_suma_fracciones(0, den1, den2, den2, x0=x, y0=y, largo=largo, alto=alto, 
                            color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                            color_background=color_background)
        y = -10
        dibujar_suma_fracciones(num1, den1, (num2 - den2), den2, x0=x, y0=y, largo=largo, alto=alto, 
                            color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                            color_background=color_background)
    
    else :
        print("Error: La fraccion a representar tiene un valor mayor que 2")
        exit()
        return


#########################################################################################
################################## SUMA_EXTENDIDA #######################################
#########################################################################################
#
# num1 -> numerador de la 1era fraccion representada
#
# den1 -> denominador de la 1era fraccion representada
#
# num2 -> numerador de la 2da fraccion representada
#
# den2 -> denominador de la 2da fraccion representada
#
# color_achurado (opcional) -> define el color de la region achurada de la fraccion
#
# color_base (opcional) -> define el color de la region no achurada de la fraccion
#
# color_lineas (opcional) -> define el color de las lineas de la representacion
#
# color_background (opcional) -> define el color del fondo de la ventana de visualizacion
#
############################################################################################
############################################################################################
def suma_extendida(num1, den1, num2, den2, color_achurado=color_achurado, 
                  color_base=color_base, color_lineas=color_lineas,
                  color_background=color_background):

    numero_achurados = num1*den2 + num2*den1
    numero_total = den1*den2
    if (numero_achurados > 2*numero_total):
        print("Error: La suma retorna un valor mayor que 2")
        exit()
        return

    dibujar_fraccion(num1, den1, "h", x0=-525, y0=75, largo=150, alto=150, 
                    color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                    color_background=color_background)
    dibujar_mas(-338, 0)
    dibujar_fraccion(num2, den2, "v", x0=-300, y0=75, largo=150, alto=150, 
                    color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                    color_background=color_background)
    dibujar_igual(-113, 0)

    dibujar_fraccion(num1, den1, "h", inter=den2, x0=-75, y0=75, largo=150, alto=150, 
                    color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                    color_background=color_background)
    dibujar_mas(112, 0)
    dibujar_fraccion(num2, den2, "v", inter=den1, x0=150, y0=75, largo=150, alto=150, 
                    color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                    color_background=color_background)
    dibujar_igual(337, 0)

    dibujar_suma_fracciones(num1, den1, num2, den2, x0=375, y0=75, largo=150, alto=150, 
                            color_achurado=color_achurado, color_base=color_base, color_lineas=color_lineas,
                            color_background=color_background)


#########################################################################################################
####################################### INPUT ###########################################################
#########################################################################################################
#
# SE PUEDE ESCOGER SOLO UNA DE LAS DIFERENTES FUNCIONES A LA VEZ, LOS EJEMPLOS SON LOS SIGUIENTES:     
#
# dibujar_fraccion(4, 0, "h")
dibujar_suma_fracciones(1, 3, 7, 5)
# suma_extendida(1, 3, 7, 5, color_achurado="purple")
#
#########################################################################################################
#########################################################################################################


### INSTRUCCION FINAL QUE PERMITE QUE LA IMAGEN DIBUJADA SE MANTENGA EN PANTALLA HASTA HACERLE CLICK ###
exitonclick()