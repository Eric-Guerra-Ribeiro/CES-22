import math
import turtle

def create_turtle():
    """
    Creates a hotpink turtle.
    """
    turt = turtle.Turtle(shape="turtle")
    turt.color("hotpink")
    turt.pensize(3)
    return turt


# Problem 1
def draw_squares(turt, n_sq, init_sz, incr_sz):
    """
    Makes the turtle turt draw n_sq squares with the same center
    and orientation. The first one with side of size init_sz and
    for each one after, its side increases by incr_sz.
    """
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    window.title("Problem 1 - Squares inside squares")
    for i in range(n_sq):
        side_sz = init_sz + i*incr_sz
        # Draws square
        turt.pendown()
        turt.forward(side_sz)
        for i in range(3):
            turt.left(90)
            turt.forward(side_sz)
        # Repositions for next square
        turt.penup()
        turt.right(45)
        turt.forward(incr_sz/math.sqrt(2))
        turt.left(135)
    window.mainloop()


# Problem 1
turt = create_turtle()
draw_squares(turt, 5, 20, 20)
