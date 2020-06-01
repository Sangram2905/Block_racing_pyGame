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

Best_score = 10
AIM = 0
xn=[]
        
player_size = 50
player_pos = [400,500]

enemy_size = 10
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
enemy_list= [enemy_pos]

SPEED = 10
def create_screen():
        screen = pygame.display.set_mode((WIDTH ,HEIGHT))
        return screen

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

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False


"""
Pseudocode
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cut-off *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value
(* Initial call *)
alphabeta(origin, depth, −∞, +∞, TRUE)
"""
#def alphabeta (screen, depth , alpha, beta,maximizingPlayer):
#       if 

screen = create_screen()

while not game_over:
    #AI Player game play
    x = player_pos[0] #horizontal movment
    y = player_pos[1]#vertical movment
    
    #print("if not game over loop")
                   
                

    for enemy_pos in enemy_list:
            
            if y == enemy_pos[1] and enemy_pos[1] >= 400 and enemy_pos[0] <= x+50 and enemy_pos[0] >= x-50 :
                    x = x
            elif enemy_pos[0] <= x+50 and enemy_pos[0] >= x-50 and enemy_pos[1] <= 300 and enemy_pos[1] >= 50 and x< 459:
                    x += 50
                    AIM +=100
            elif x > 460 and enemy_pos[0] <= x+50 and enemy_pos[0] >= x-50 and enemy_pos[1] >= 301:
                    x -= 50
                    AIM +=100
            
            if x in range (-50,10):
                    x += player_size
                    AIM +=100
            if x in range (800,850):
                    x -= player_size
                    AIM +=100
    
    player_pos = [x,y]
    
    delay = random.random()
       
    for idx, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1]>=0 and enemy_pos[1] < HEIGHT:
                    enemy_pos[1] += SPEED
            else :
                    enemy_pos[0] = random.randint(0,WIDTH-enemy_size)
                    enemy_pos[1] = 0
                    SCORE += 1
                    if Best_score < SCORE:
                            Best_score = SCORE
    if len(enemy_list) < 5 and delay < 0.1:
        x_pos = random.randint(0,750)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
               
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()             
            
    #print(event)
    print(x,enemy_list)
    #print(SCORE)
    #print(enemy_pos[0],enemy_pos[1])
    
    #print(en_x,en_y)
    
    
    screen.fill(Background_color)
                
    if SCORE > 100:
        Best_score = SCORE

    if SCORE >= 0 and SCORE < 15:
        SPEED = 5
    elif SCORE >= 15 and SCORE < 35:
        SPEED = 7
    elif SCORE >= 35 and SCORE < 55:
        SPEED = 8
    elif SCORE >= 55 and SCORE < 75:
        SPEED = 9
    elif SCORE >= 75:
        SPEED = 10

        
    if collision_check(enemy_list, player_pos):
            game_over = True
            break
    
        
    
    for enemy_pos in enemy_list:
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
    




    
    
