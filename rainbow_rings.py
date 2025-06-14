import turtle
t= turtle.Turtle()
t.speed(10)
colors= ['yellow','orange','red','pink','violet','indigo','blue','green']
turtle.bgcolor('black')

for i in range(36):
    t.color(colors[i%8])
    t.circle(100)
    t.right(10)
turtle.done()
