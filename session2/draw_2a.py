from turtle import *

for edge in range(3,10):
    print(edge)
    for i in range(edge):
        forward(100)
        left(360/edge)
mainloop()