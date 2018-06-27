import pygame
import random
from sys import exit
environment=[]
class maze_box:

    def __init__(self,init_x,init_y):
        self.init_x=init_x
        self.init_y=init_y
        self.final_x=init_x+60
        self.final_y=init_y+30
        self.nature=0
        self.score=0
        self.color=(255,255,255)
        choice=random.randint(1,10)
        if init_x==0 and init_y==0:
            choice=-1
            self.nature=-1
            self.score=0
            self.color=(255,255,0)
        if final_x==600 and final_y==300:
            choice=-2
            self.nature=-2
            self.score=100
            self.color=(0,255,0)
        if choice>0:
            if choice>4:
                self.nature=0
                self.score=-1
            else:
                self.nature=1
                self.score=-100
                self.color=(0,0,255)

if __name__=='__main__':
    pygame.init()
    size=(600,300)
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("AI MAZE")
    clock=pygame.time.Clock()
    screen.fill((255,255,255))
    #pygame.draw.rect(screen,(255,0,0),(55,50,20,25))
    #pygame.draw.line(screen,(0,0,0),(0,0),(100,0),4)
    #pygame.draw.line(screen,(0,0,0),(100,0),(100,100),4)
    for i in range(0,10):
        for j in range(0,10):
            init_x=(60*i)%600
            init_y=(30*j)%300
            final_x=init_x+60
            final_y=init_y+30
            
            pygame.draw.rect(screen,(0,0,0),(init_x,init_y,final_x,final_y),1)
    pygame.display.update()   
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
    
