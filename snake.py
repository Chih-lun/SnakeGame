import pygame

WHITE = (255,255,255)

class Snake:
    def __init__(self):
        self.direction = 'R'
        self.head = [250,250]
        self.segements = [self.head,[230,250],[210,250]]

    def turn_right(self):
        if not self.direction == 'L':
            self.direction = 'R'

    def turn_left(self):
        if not self.direction == 'R':
            self.direction = 'L'

    def turn_up(self):
        if not self.direction == 'DOWN':
            self.direction = 'UP'

    def turn_down(self):
        if not self.direction == 'UP':
            self.direction = 'DOWN'

    def show_head(self,window):
        pygame.draw.rect(window,WHITE,(self.head[0],self.head[1],20,20))

    def show_body(self,window):
        for i in self.segements:
            pygame.draw.rect(window,WHITE,(i[0],i[1],20,20))

    def move(self):
        for i in range(len(self.segements)-1,0,-1):
            self.segements[i][0] = self.segements[i-1][0]
            self.segements[i][1] = self.segements[i-1][1]
        if self.direction == 'R':
            self.head[0] = self.head[0] + 10
        elif self.direction == 'L':
            self.head[0] = self.head[0] - 10
        elif self.direction == 'UP':
            self.head[1] = self.head[1] - 10
        elif self.direction == 'DOWN':
            self.head[1] = self.head[1] + 10

    def extend(self):
        if self.direction == 'R':
            self.segements.append([self.segements[-1][0]-20,self.segements[-1][1]])
        elif self.direction == 'L':
            self.segements.append([self.segements[-1][0]+20,self.segements[-1][1]])
        elif self.direction == 'UP':
            self.segements.append([self.segements[-1][0],self.segements[-1][1]+20])
        elif self.direction == 'DOWN':
            self.segements.append([self.segements[-1][0],self.segements[-1][1]-20])