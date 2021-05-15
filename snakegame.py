import pygame
import time
from snake import Snake
from food import Food
from message import Message

#colors
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 216, 0)

class Snakegame:
    def __init__(self):
        #set up the pygame
        pygame.init()
        pygame.display.set_caption('Snake Game')
        self.win = pygame.display.set_mode((500,500))
        self.fps = pygame.time.Clock()
        self.game_on = True
        #snake attribute
        self.snake = Snake()
        #food attribute
        self.food = Food()
        #scoreboard attribute
        self.score = 0
        self.scoreboard = Message(50)
        #gameover_message attribute
        self.gameover_message = Message(50)

    def run(self):
        #game process
        while self.game_on:
            #fps set up
            self.fps.tick(25)

            #event controll
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake.turn_right()
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn_left()
                    elif event.key == pygame.K_UP:
                        self.snake.turn_up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn_down()

            #window color
            self.win.fill(BLACK)

            #show scoreboard
            self.scoreboard.show_text(self.win,f'Your score: {self.score}',YELLOW,[135,0])

            #draw head
            self.snake.show_head(self.win)

            #draw food
            self.food.show_food(self.win)

            #draw body
            self.snake.show_body(self.win)

            #move body
            self.snake.move()

            #touch the food
            if abs(self.food.foodx-self.snake.head[0]) < 12 and abs(self.food.foody-self.snake.head[1]) < 12:
                #refresh the position
                self.food.refresh_position()
                self.score = self.score + 1
                print('yummy')

                #grow up
                self.snake.extend()

            #game_over
            if self.snake.head[0] > 500 or self.snake.head[1] > 500 or self.snake.head[0] < 0 or self.snake.head[1] < 0:
                self.game_on = False
            for i in self.snake.segements[1:]:
                if self.snake.head == i:
                    self.game_on = False

            #screen update
            pygame.display.update()

        #show gameover_message
        self.gameover_message.show_text(self.win,'You lost',RED,[200,200])
        pygame.display.update()
        time.sleep(3)

        pygame.quit()
