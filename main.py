#!/bin/python
import pygame
import random
from math import sin, pi
# Define some colors
APPLE_COL = (255, 0, 0)
SNAKE_HEAD_COL = (0, 0, 0)
SNAKE_TAIL_COL = (255,255,255)
BACKGROUND_COL = (0, 100, 0)

NORMAL_SPEED = 10
POWERUP_SPEED = 3
POWERUP_TIME = 100

pygame.init()

size = (600, 600)
grid_size = (20, 20)
cell_size = (size[0]/grid_size[0], size[1]/grid_size[1])

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

pygame.font.init()
font = pygame.font.SysFont('FuraMono Nerd Font Regular', 50)
font_big = pygame.font.SysFont('FuraMono Nerd Font Regular', 100)

clock = pygame.time.Clock()

def randomNom():
    return "audio/" + ["nom1.wav","nom2.wav","nom3.wav","nom4.wav","nom5.wav","nom6.wav","nom7.wav","nom8.wav"][random.randrange(0,8)]

def randomStar():
    return "audio/" + ["star1.wav","star2.wav","star3.wav","star4.wav",][random.randrange(0,4)]


def draw_cell(coord, color):
    screen_coord = [
        coord[0]*cell_size[0],
        coord[1]*cell_size[1],
        cell_size[0],
        cell_size[1]
    ]
    pygame.draw.rect(screen, color, screen_coord, 0)


counter = 0
move_counter = 0

done = False
while not done:
    game_done = False
    ori = (0, 1)
    snake = [(2, 2), (2, 3), (2, 4)]
    apple = (3, 3)
    speed = NORMAL_SPEED
    powerup = 0
    while not game_done and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ori = (0, -1)
                if event.key == pygame.K_s:
                    ori = (0, 1)
                if event.key == pygame.K_a:
                    ori = (-1, 0)
                if event.key == pygame.K_d:
                    ori = (1, 0)

        screen.fill(BACKGROUND_COL)

        counter += 1
        if (counter % speed == 0):
            move_counter += 1

            if powerup > 0:
                powerup -= 1
                if powerup == 0:
                    pygame.mixer.music.stop()
                speed = POWERUP_SPEED
            else:
                speed = NORMAL_SPEED
            head = snake[len(snake)-1]
            new_head = (
                head[0] + ori[0],
                head[1] + ori[1]
            )

            if new_head in snake and powerup == 0:
                game_done = True
            if not (new_head[0] < grid_size[0] and new_head[1] < grid_size[1] and new_head[0] >= 0 and new_head[1] >= 0):
                if powerup != 0:
                    new_head = (
                        new_head[0] % grid_size[0],
                        new_head[1] % grid_size[1],
                    )
                else: 
                    game_done = True
            
            snake.append(new_head)

            if head == apple:
                pygame.mixer.music.load(randomNom())
                pygame.mixer.music.play(0)
                pygame.mixer.music.queue(randomStar())
                apple = (
                    random.randrange(0, grid_size[0]),
                    random.randrange(0, grid_size[1])
                )
                powerup = POWERUP_TIME
                speed = POWERUP_SPEED

            else:
                snake.pop(0)

        draw_cell(apple, APPLE_COL)
        for i,pos in enumerate(snake):
            progress = i / len(snake)
            if powerup > 0:
                rainbow_offset = move_counter / -4
                rainbow_scale = 0.5
                col = (
                    sin(i*rainbow_scale+rainbow_offset+(0/3*pi)) * 128 + 128,
                    sin(i*rainbow_scale+rainbow_offset+(1/3*pi)) * 128 + 128,
                    sin(i*rainbow_scale+rainbow_offset+(2/3*pi)) * 128 + 128
                )
            else: 
                col = (
                    SNAKE_TAIL_COL[0] * progress + SNAKE_HEAD_COL[0] * (1 - progress),
                    SNAKE_TAIL_COL[1] * progress + SNAKE_HEAD_COL[1] * (1 - progress),
                    SNAKE_TAIL_COL[2] * progress + SNAKE_HEAD_COL[2] * (1 - progress),
                )
            draw_cell(pos, col)

        if not game_done:
            surface = font.render("Score {0}".format(len(snake)),False,(100,0,100))
            screen.blit(surface,(0,0))

        pygame.display.flip()

        clock.tick(60)
    
    if done: break
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/ded1.wav")
    pygame.mixer.music.play(0)

    gameover_done = False
    while not gameover_done and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameover_done = True
        
        surface = font_big.render("u ded lol",False,(255,0,0))
        screen.blit(surface,(0,0))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
