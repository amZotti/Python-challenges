import turtle

def main():
    radius = 100
    turtle.speed(0)

    for rings in range(10):
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.circle(radius)
        radius += 10

if __name__ == "__main__":
    main()
