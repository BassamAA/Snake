from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
F = "fastest"
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.ps = []
        self.create_snake()
        self.head = self.ps[0]

    def create_snake(self):
        for p in STARTING_POSITION:
            self.add_segment(p)

    def add_segment(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.ps.append(new_part)

    def extend(self):
        self.add_segment(self.ps[-1].position())

    def move(self):
        for p in range(len(self.ps) -1, 0, -1):
            new_x = self.ps[p - 1].xcor()
            new_y = self.ps[p - 1].ycor()
            self.ps[p].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 270 and self.head.heading() != UP :
            self.head.setheading(270)


    def right(self):
        if self.head.heading() != 0 and self.head.heading() != LEFT:
            self.head.setheading(0)


    def left(self):
        if self.head.heading() != 180 and self.head.heading() != RIGHT:
            self.head.setheading(180)







