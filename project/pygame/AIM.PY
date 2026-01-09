import pygame
import random 
import math

pygame.init()

width ,height = 800, 600
win = pygame.display.set_mode(width, height)
pygame.display.set_caption("AIM Trainer")

target_increase = 400
target_event = pygame.USEREVENT 

target_padding = 90
b6_color = (20,30,40)
target_color =(255,50,50)
top_bar_height = 50
target_font = pygame.font.SysFont('comicsans', 30)


class Target:
    max_size = 50
    growth_rate = 1.5
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.alive = True
        
    def update(self):
        if self.size < self.max_size:
            self.size += self.growth_rate
        else:
            self.alive = False
                
    def draw(self, win):
        pygame.draw.circle(win, target_color, (self.x, self.y), int(self.size))
        