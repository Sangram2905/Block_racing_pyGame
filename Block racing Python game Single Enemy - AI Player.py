# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:49:47 2020

@author: Sangram Phadke
"""
import sys
import random
import pygame
import math

pygame.init()

WIDTH = 800 
HEIGHT = 600
RED = (255,0,0)
BLUE = (0,0,255)
Background_color = (0,0,0)
SCORE = 0
NSCORE = 0

Best_score = 99

        
player_size = 50
player_pos = [400,500]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
enemy_list= [enemy_pos]

SPEED = 10
   
screen = pygame.display.set_mode((WIDTH ,HEIGHT))

game_over = False
clock = pygame.time.Clock()
print_score = pygame.font.SysFont("monospace",30)
print_Best_score = pygame.font.SysFont("monospace",30)    
    
def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

while not game_over:
    #AI Player game play
    x = player_pos[0] #horizontal movment
    y = player_pos[1] #vertical movment
    print("if not game over loop")
    if x in range (50,450):
            if enemy_pos[0] <= x+50 and enemy_pos[1] >= 400 :
                    x += player_size
    if x in range (350,750):
            if enemy_pos[0] >= x-50 and enemy_pos[1] >= 400:
                    x -= player_size
    if x in range (-100,50):
            if enemy_pos[0] >= x and enemy_pos[1] >= 400:
                    x += player_size
    if x in range (700,850):
            if enemy_pos[0] <= x and enemy_pos[1] >= 400:
                    x -= player_size                       
                  
    player_pos = [x,y]
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
                                

                
                

            
    #print(event)
    print(x,y)
    print(SCORE)
    print(enemy_pos[0],enemy_pos[1])
    
    #print(en_x,en_y)
    
    
    screen.fill(Background_color)
    
    if enemy_pos[1]>=0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += SPEED
    else :
        enemy_pos[0] = random.randint(0,WIDTH-enemy_size)
        enemy_pos[1] = 0
        SCORE += 1
        
    if SCORE > 100:
        Best_score = SCORE

    if SCORE >= 0 and SCORE < 15:
        SPEED = 10
    elif SCORE >= 15 and SCORE < 35:
        SPEED = 20
    elif SCORE >= 35 and SCORE < 55:
        SPEED = 30
    elif SCORE >= 55 and SCORE < 75:
        SPEED = SCORE
    elif SCORE >= 75:
        SPEED = 100

        
    if detect_collision(player_pos,enemy_pos):
        game_over = True
    
        
    
    pygame.draw.rect(screen,BLUE,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
    
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    
    score_text = "Score: "+str(SCORE)
    best_score_text = "Best Score: "+str(Best_score)

    
            
    label = print_score.render(score_text,1,(255,255,0))
    label1 = print_Best_score.render(best_score_text,1,(255,255,200))
    
    screen.blit(label,(WIDTH-250,HEIGHT-50))
    screen.blit(label1,(WIDTH-700,HEIGHT-50))
    clock.tick(30)
    pygame.display.update()
    




    
    
