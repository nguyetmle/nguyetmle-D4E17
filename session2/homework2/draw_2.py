from turtle import *

for edge in range(3,7):
    for i in range(edge):
        if edge % 2 == 0:
            color('red')
        else:
            color('blue')
        forward(100)
        left(360/edge)

mainloop()

