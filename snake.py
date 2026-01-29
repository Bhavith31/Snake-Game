from turtle import Turtle

class Snake:
    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(x, 0)
            x -= 20
            self.all_snake.append(t)

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position.xcor(), position.ycor())
        self.all_snake.append(t)

    def extend(self):
        self.add_segment(self.all_snake[-1])

    def move(self):
        for i in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[i - 1].xcor()
            new_y = self.all_snake[i - 1].ycor()
            self.all_snake[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
