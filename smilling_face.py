import turtle

#screen settings
s=turtle.Screen()
s.title("Smilling Face Animation")
s.bgcolor("light blue")

#pen settings
p=turtle.Turtle()
p.speed(5)
p.color("yellow")

#head
p.begin_fill()
p.circle(100)
p.end_fill()

#eyes
p.up()
p.goto(50,130)
p.color("black")
p.down()
p.begin_fill()
p.circle(10)
p.end_fill()
p.up()
p.goto(-50,130)
p.down()
p.begin_fill()
p.circle(10)
p.end_fill()

#arm and leg
p.pensize(5)
p.up()
p.goto(0,0)
p.right(90)
p.down()
p.forward(150)
p.right(30)
p.forward(100)
p.up()
p.goto(0,-150)
p.left(60)
p.down()
p.forward(100)
p.up()
p.goto(0,-50)
p.right(60)
p.down()
p.forward(100)
p.up()
p.goto(0,-50)
p.left(60)
p.down()
p.forward(100)
p.up()
p.goto(-50,80)
p.right(30)
p.down()
p.pensize(5)

#mouth
for i in range(60):
    p.forward(2.5)
    p.left(3)

#cursor
p.up()
p.goto(0,-1000)
p.down()

turtle.mainloop()