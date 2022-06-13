from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.title("SNakE GaMe")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()  # Creating obj of the class
food = Food()
score = Score()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game = True
while game:
    screen.update()
    time.sleep(.1)  # screen is going to update every .1 second
    snake.move()

    if snake.head.distance(food) < 15:
        score.current_score()
        snake.levelup()
        food.new_food_loc()

    for i in snake.snake_Len[1:]:
        if snake.head.distance(i) < 10:
            score.game() 
            break        
  

    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
        score.game()
        break

screen.exitonclick()