import turtle
colors=['pink','red','purple','cyan','white','yellow','blue']

t= turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')

for i in range(200):
    t.color(colors[i%6])
    t.fd(i*6)
    t.left(200)
    t.width(2)
