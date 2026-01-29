from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.tracer(0)
s.title("My Snake Game")

game_status=False

snake=Snake()
food=Food()
scoreboard=Scoreboard()
    
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_status=True
while game_status:
    s.update()
    time.sleep(0.1)
    snake.move()
        
    if snake.head.distance(food)<15:
        food.location()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 :
        game_status=False
        scoreboard.game_over()     
        
    for segment in snake.all_snake[1:]:  
        if snake.head.distance(segment) < 10:
            game_status = False
            scoreboard.game_over()

s.exitonclick()