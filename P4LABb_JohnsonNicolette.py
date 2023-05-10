import turtle
win =  turtle.Screen()
t = turtle.Turtle()

t.color("pink")
t.pensize(8)

# Letter N
t.left(90)
t.forward(100)
t.right(140)
t.forward(130)
t.left(140)
t.forward(100)

# transition
t.penup()
t.right(90)
t.forward(40)



# Letter J
t.pendown()
t.forward(100)
t.left(180)
t.forward(50)
t.left(90)
t.forward(100)
t.right(90)
t.forward(48)
t.right(90)
t.forward(36)

win.mainloop()  