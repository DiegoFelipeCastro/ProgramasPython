# El codigo solicita al usuario por consola el numero de particiones que desea realizar para dibujar el trinagulo de sierpinski
from turtle import*

setup(1350, 700, 0, 0)
screensize(3000, 3000)
bgcolor("light cyan")
right(30) # Cambia la inclinacion de todo el conjunto de triangulos
pu()# Quita las lineas
ht()# Quita el cursor que dibuja (turtle)

speed(100)

def sierpinski(tamañoTriangulo,particiones):
    if particiones == 0:
        stamp()# Relleno del triangulo
    else:
        for i in range(0,3):
            forward(tamañoTriangulo)# Avanza y pinta segun el tamaño de cada triangulo
            sierpinski(tamañoTriangulo/2, particiones-1)
            backward(tamañoTriangulo)# Se devuelve al punto incial de cada trinagulo
            left(120)# Cambia la inclinacion de cada triangulo

particiones= int(input("Ingrese valor para dibujar el triangulo: "))
if particiones <= 5:
    shape("triangle")# La figura del relleno
sierpinski((particiones*40),particiones)
exitonclick()# Cierra la ventana cuando se le da un click
