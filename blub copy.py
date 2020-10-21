#!/bin/python
import pygame
import random

# Define some colors
APPLE_COL = (255, 0, 0)
SNAKE_COL = (0, 0, 0)
BACKGROUND = (0, 100, 0)

pygame.init()

size = (600, 600)
grid_size = (20, 20)
cell_size = (size[0]/grid_size[0], size[1]/grid_size[1])

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

pygame.font.init()
font = pygame.font.SysFont('FuraMono Nerd Font Regular', 100)

clock = pygame.time.Clock()

# 1 snake, 2 apple


def draw_cell(coord, type):
    if type == 1:
        color = SNAKE_COL
    elif type == 2:
        color = APPLE_COL
    else:
        raise Exception("Diese farbe gibts nicht.")
    screen_coord = [
        coord[0]*cell_size[0],
        coord[1]*cell_size[1],
        cell_size[0],
        cell_size[1]
    ]
    pygame.draw.rect(screen, color, screen_coord, 0)


counter = 0

done = False
while not done:
    game_done = False
    ori = (0, 1)
    snake = [(2, 2), (2, 3), (2, 4)]
    apple = (3, 3)

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

        screen.fill(BACKGROUND)

        counter += 1
        if (counter % 20 == 0):
            head = snake[len(snake)-1]
            new_head = (
                head[0] + ori[0],
                head[1] + ori[1]
            )

            if new_head in snake:
                game_done = True
            if not (new_head[0] < grid_size[0] and new_head[1] < grid_size[1] and new_head[0] >= 0 and new_head[1] >= 0):
                game_done = True
            
            snake.append(new_head)

            if head == apple:
                apple = (
                    random.randrange(0, grid_size[0]),
                    random.randrange(0, grid_size[1])
                )
            else:
                snake.pop(0)

        draw_cell(apple, 2)
        for pos in snake:
            draw_cell(pos, 1)

        pygame.display.flip()

        clock.tick(60)
    
    gameover_done = False
    while not gameover_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                gameover_done = True
        
        surface = font.render("u ded lol",False,(255,0,0))
        screen.blit(surface,(0,0))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
