from turtle import * # lên docs.python.org đọc về các lệnh của turtle

speed(-1)
for i in range(15000): # vòng lặp lại 3 lần
    forward(100) # độ dài đường vẽ thẳng  #block of code
    left(90) # góc xoay trái
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

    right(7)

mainloop() # mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.