import turtle
import time
import math

def draw_poly(turt, n, sz):
    """
    Makes the turtle turt draw a regular polyon
    of n sides, each with size sz.
    """
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    window.title("Problem 2 - Polygon")
    angle = 360/n
    # Draws polygon
    turt.pendown()
    for i in range(n):
        turt.forward(sz)
        turt.left(angle)
    time.sleep(1)

def main():
    """
    Draws a regular octagon with a turtle.
    """
    turt = turtle.Turtle(shape="turtle")
    turt.color("hotpink")
    turt.pensize(3)
    turt.penup()
    turt.goto(60, -25*(1+math.sqrt(2)))
    draw_poly(turt, 8, 50)

if __name__ == "__main__":
    main()
