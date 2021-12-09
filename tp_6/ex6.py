from turtle import *

def triangle(a: int):
    for _ in range(3):
        forward(a)
        left(120)

def polygone(n: int, a: int):
    for _ in range(n):
        forward(a)
        left(360/n)

def koch(n: int, a: float):
    if n == 0:
        forward(a)
    else:
        koch(n - 1, a/3)
        left(60)
        koch(n - 1, a/3)
        right(120)
        koch(n - 1, a/3)
        left(60)
        koch(n - 1, a/3)

def flocon(n: int, a: int):
    for _ in range(3):
        koch(n, a)
        right(120)

def flocon_jolie(n: int, a: int):  # Pareil, sauf qu'on tourne dans l'autre sens (c'est joli ☺)
    for _ in range(3):
        koch(n, a)
        left(120)


l = 800  # Longueur d'un côté

speed(500)  # On accelère le tracé

# Placement pour que le motif soit centré (à peu près)
penup()
goto(-l/2, l/3)
pendown()

flocon(5, l)  # On trace
