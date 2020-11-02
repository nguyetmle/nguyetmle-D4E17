from turtle import *

for i in range(4):
    forward(100)
    left(360/4)
for i in range(3): #số trong range là số cạnh của hình
    forward(100)
    left(360/3)
for i in range(5):
    forward(100)
    left(360/5)
mainloop()

for edge in range(3,6):
    print(edge)
    for i in range(edge):
        forward(100)
        left(360/edge)
mainloop()

