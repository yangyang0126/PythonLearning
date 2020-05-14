import turtle 

star = turtle.Turtle()


def draw_star(*args):
  for argument in args:
    star.pencolor(argument)
    for i in range(5):
      star.forward(80)
      star.right(144)
draw_star("green","blue","yellow","pink","red","purple","orange")    
turtle.done()
