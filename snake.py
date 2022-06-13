from turtle import Turtle,Screen
screen = Screen()
POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST =20
UP=90
DOWN=270
LEFT=180
RIGHT=0
#You can define a constant by making it all "CAPS"
class Snake: #creating a class Snake
    def __init__(self):
        #Attributes every time we create an object
        #It will create the snake with three blocks
        self.snake_Len = []
        self.create_snake()
        self.head=self.snake_Len[0]


    def create_snake(self):
        for i in POS:
            self.add_snake(i)

    def add_snake(self,i):
        snake_create = Turtle(shape="square")
        snake_create.penup()
        snake_create.color("white")
        snake_create.setpos(i)
        self.snake_Len.append(snake_create)

    def move(self):
        for s in range(len(self.snake_Len) - 1, 0, -1):
            new_x = self.snake_Len[s - 1].xcor()
            new_y = self.snake_Len[s - 1].ycor()
            self.snake_Len[s].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def levelup(self):
        self.add_snake(self.snake_Len[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)