import turtle
import tkinter

win = turtle.Screen()
kame = turtle.Turtle()
kame.shape('turtle')

for _ in range(6):
    kame.forward(100)
    kame.left(120)
    kame.forward(100)
    kame.left(120)
    kame.forward(100)
    kame.left(180)

kame.forward(100)

kame.color('red')
kame.pensize(10)
kame.left(90)
kame.circle(100)

win.mainloop()