import pygame

class Message:
    def __init__(self,size):
        self.the_message = pygame.font.SysFont(None,size)


    def show_text(self,window,context,color,position):
        self.message = self.the_message.render(context,True,color)
        window.blit(self.message,position)