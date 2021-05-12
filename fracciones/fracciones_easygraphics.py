from easygraphics import *

# Definiendo variables globales

# Colores
color_lineas = Color.BLACK
color_base = Color.WHITE
color_achurado = Color.BLUE

# Dimension ventana
largo_img = 500
alto_img = 500

# Dimensiones representacion fraccion
ancho_lineas = 5
largo = 400
alto = 400
x0 = 50
y0 = 50

# Funcion que dibuja un rectangulo con origen en (x0, y0)
def dibujar_rectangulo(x0, y0, largo, alto):
    draw_polygon(x0, y0, (x0+largo), y0, (x0+largo), (y0+alto), x0, (y0+alto))

# Funcion dibuja la representacion de una fraccion, especificando su numerador y denominador
# Se puede escoger entre una representacion horizontal o vertical
def dibujar_fraccion(numerador, denominador, mode):
    x = x0
    y = y0
    if (mode == "vertical"):
        delta_x = largo/denominador
        set_fill_color(color_achurado)
        for i in range(numerador):
            dibujar_rectangulo(x, y, delta_x, alto)
            x = x + delta_x
        set_fill_color(color_base)
        for i in range(denominador-numerador):
            dibujar_rectangulo(x, y, delta_x, alto)
            x = x + delta_x
    elif (mode == "horizontal"):
        delta_y = alto/denominador
        set_fill_color(color_achurado)
        for i in range(numerador):
            dibujar_rectangulo(x, y, largo, delta_y)
            y = y + delta_y
        set_fill_color(color_base)
        for i in range(denominador-numerador):
            dibujar_rectangulo(x, y, largo, delta_y)
            y = y + delta_y

# Funcion que dibuja la suma de 2 fracciones, representadas cada una con "num" (numerador) y "den" (denominador).
# La suma de ambas fracciones debe ser < que 1 (o me muero UnU).
def dibujar_suma_fracciones(num1, den1, num2, den2):
    x = x0
    y = y0
    delta_x = largo/den2
    delta_y = alto/den1
    numero_achurados = num1*den2 + num2*den1
    numero_total = den1*den2
    set_fill_color(color_achurado)
    for i in range(numero_achurados):
        dibujar_rectangulo(x, y, delta_x, delta_y)
        if (x >= x0 + (delta_x*(den2 - 1)) - ancho_lineas):
            x = x0
            y = y + delta_y
        else:
            x = x + delta_x
    set_fill_color(color_base)
    for i in range(numero_total - numero_achurados):
        dibujar_rectangulo(x, y, delta_x, delta_y)
        if (x >= x0 + (delta_x*(den2 - 1)) - ancho_lineas):
            x = x0
            y = y + delta_y
        else:
            x = x + delta_x

# Metodos realizan las operaciones pedidas por el/la usuario/a, y guardan la imagen obtenida en formato PNG
# en el directorio donde se encuentre el script.
def fraccion(numerador, denominador, modo):
    init_graph(largo_img, alto_img)
    set_line_width(ancho_lineas)
    set_color(color_lineas)
    dibujar_fraccion(numerador, denominador, modo)
    save_image("frac_" + str(numerador) + "." + str(denominador) + "_" + modo + ".png")
    pause()
    close_graph()

def suma_fracciones(num1, den1, num2, den2):
    init_graph(largo_img, alto_img)
    set_line_width(ancho_lineas)
    set_color(color_lineas)
    dibujar_suma_fracciones(num1, den1, num2, den2)
    save_image("frac_" + str(num1) + "." + str(den1) + "+" + str(num2) + "." + str(den2) + ".png")
    pause()
    close_graph()


# INPUT se ingresa como se muestra en los ejemplos:
#fraccion(3, 5, "vertical")
#suma_fracciones(2, 5, 3, 10)

#fraccion(7, 11, "vertical")
suma_fracciones(3, 5, 3, 4)