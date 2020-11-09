from turtle import *

color_list = ['red', 'yellow', 'blue', 'black', 'gray', 'brown', 'purple', 'red']
for i in range(len(color_list)):
    color(i)
    for edge in range(3,8):
        print(edge)
        for j in range(edge):
            forward(100)
            left(360/edge)
end_fill()
mainloop()

