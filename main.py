from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list("ABCDEFGHIJKLMNOPQRSTUVWXYZÑ123456") * 2 #Ocupe letras y numeros para poder mejorar el entendimiento 
state = {'mark': None, 'taps': 0}  # Contador de taps
hide = [True] * 64


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1  # Incrementar contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibujar cuadrados ocultos
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Mostrar número seleccionado si hay marca activa
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 12, y+11)
        color('black')
        write(tiles[mark] ,font=('Arial', 30, 'normal'))

    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 16, 'normal'))

    if not any(hide):
        up()
        goto(-50, 0)
        color('green')
        write('¡Juego terminado!', font=('Arial', 20, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()