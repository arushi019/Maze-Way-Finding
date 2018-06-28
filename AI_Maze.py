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
        if init_x==0 and init_y==0:
            self.nature=-1
            self.score=0
            self.color=(255,255,0)
        if final_x==600 and final_y==300:
            self.nature=-2
            self.score=100
            self.color=(0,255,0)

class player:

    def __init__(self):
        self.score=0
        self.x=0
        self.y=0
        self.current_index=0

    def get_current_index(self):
        return self.x*10+self.y

    def update_index(self,dir):
        if dir==1:
            self.x=self.x+1
        if dir==-1:
            self.x=self.x-1
        if dir==2:
            self.y=self.y+1
        if dir==-2:
            self.y=self.y-1

    def valid_right(self):
        index=self.get_current_index()
        x=self.x
        y=self.y
        if x>=9 or x<0:
            return False
        if environment[index+1].nature==1:
            return False
        return True

    def valid_left(self):
        index=self.get_current_index()
        x=self.x
        y=self.y
        if x>9 or x<=0:
            return False
        if environment[index-1].nature==1:
            return False
        return True

    def valid_top(self):
        index=self.get_current_index()
        x=self.x
        y=self.y
        if y>9 or y<=0:
            return False
        if environment[index-10].nature==1:
            return False
        return True

    def valid_bottom(self):
        index=self.get_current_index()
        x=self.x
        y=self.y
        if y>=9 or y<0:
            return False
        if environment[index+10].nature==1:
            return False
        return True

    def make_decision(self):
        d=random.randint(0,3)
        if d==0:
            if self.valid_right()==True:
                self.update_index(1)
        if d==1:
            if self.valid_left()==True:
                self.update_index(-1)
        if d==2:
            if self.valid_top()==True:
                self.update_index(2)
        if d==3:
            if self.valid_bottom()==True:
                self.update_index(-2)

    def at_finish(self):
        if self.x==9 and self.y==9:
            return True
        return False

    def update_score(self):
        if self.at_finish()==False:
            self.score=self.score-1
        else:
            self.score=self.score+100

def set_walls():
    for i in range(1,9):
        start=random.randint(0,9)
        for j in range(0,3):
            current=start+j
            if current>9:
                current=current-10
            index=i*10+current
            environment[index].nature=1
            environment[index].color=(0,0,255)
            

if __name__=='__main__':
    pygame.init()
    size=(600,300)
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("AI MAZE")
    clock=pygame.time.Clock()
    p=player()
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
            temp=maze_box(init_x,init_y)
            environment.append(temp)
            #print(temp.init_x,temp.init_y,temp.nature,temp.color)
    set_walls()
    for i in range(0,10):
        for j in range(0,10):
            init_x=(60*i)%600
            init_y=(30*j)%300
            final_x=init_x+60
            final_y=init_y+30
            temp=environment[i*10+j]
            if temp.nature==1:
                temp.score=-1000
            elif temp.nature==0:
                temp.score=-1
            print(temp.init_x,temp.init_y,temp.nature,temp.color)
            pygame.draw.rect(screen,temp.color,(init_x,init_y,final_x,final_y),0)
            pygame.draw.rect(screen,(0,0,0),(init_x,init_y,final_x,final_y),1)
    pygame.display.update()   
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pygame.draw.circle(screen,(255,0,0),[p.x*60+30,p.y*30+15],10)
                pygame.display.update()
                print(p.score)
                p.make_decision()
                p.update_score()
                if p.at_finish()==True:
                    print("Have reached the aim")
                    pygame.quit()
                    exit()
