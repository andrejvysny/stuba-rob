import pygame
from pygame.locals import *
import math
import sys

pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Differential Drive")
clock = pygame.time.Clock()

player_radius = 5
wheel_radius = 2

x=screen_width/2
y= screen_height/2
Vt = 0
dphi = 0
L = 200
phi = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_w:
                Vt += 0.2
            elif event.key == K_s:
                Vt -= 0.2
            elif event.key == K_a:
                dphi -= 0.1
            elif event.key == K_d:
                dphi += 0.1
            elif event.key == K_q:
                phi = 0
                dphi = 0
            elif event.key == K_r:
                Vt = 0
            elif event.key == K_SPACE:
                Vt = 0
                phi = 0
                dphi = 0
                x=screen_width/2
                y= screen_height/2

    phi += math.radians(dphi)
    Vt_x = Vt * math.cos(phi)
    Vt_y = Vt * math.sin(phi)

    x += Vt_x
    y += Vt_y

    x_l = x + math.cos(phi + math.pi/2)*(L/2)
    y_l = y + math.sin(phi + math.pi/2)*(L/2)

    x_r = x - math.cos(phi + math.pi/2)*(L/2)
    y_r = y - math.sin(phi + math.pi/2)*(L/2)

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255,255,255), (x,y), player_radius)
    pygame.draw.circle(screen, (255,50,50), (x_r,y_r), wheel_radius)
    pygame.draw.circle(screen, (50,255,50), (x_l,y_l), wheel_radius)

    pygame.display.update()
    clock.tick(60)
