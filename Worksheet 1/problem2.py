import turtle

def draw_poly(turt, n, sz):
    """
    Makes the turtle turt draw a regular polyon
    of n sides, each with size sz.
    """
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    window.title("Problem 2 - Polygon")
    angle = 360/n
    for i in range(n):
        turt.pendown()
        turt.forward(sz)
        turt.left(angle)
    window.mainloop()


turt = turtle.Turtle(shape="turtle")
turt.color("hotpink")
turt.pensize(3)
draw_poly(turt, 8, 50)
