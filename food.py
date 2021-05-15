import pygame
import random

BLUE = (0, 0, 255)

class Food:
    def __init__(self):
        self.refresh_position()

    def show_food(self,window):
        pygame.draw.rect(window,BLUE,(self.foodx,self.foody,10,10))

    def refresh_position(self):
        self.foodx = random.randint(50,450)
        self.foody = random.randint(50,450)