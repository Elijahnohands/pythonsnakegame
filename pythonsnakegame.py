import pygame
import time
import random
pygame.init()

dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width,dis_height)) # creates the display and defines its size

pygame.display.set_caption('Snake game by Elijahnohands') # I think this names the window 

blue = (0, 0, 255) # inititalizing colors used 
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


clock = pygame.time.Clock()

snake_speed = 10 # sets speed of snake / game
snake_block = 10
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop(): # creating a function
    game_over = False #initilizes the game over state
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block))
    foody = round(random.randrange(0, dis_height - snake_block))

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("you Lost! Press Q-Quit or C-Play Again")
            pygame.display.update()

            for event in pygame.event.get():
                if event.key == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get(): # creates the proper quit event when pressing x
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: # create the keyboard inputs to move snake
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 :
            game_over = True

        x1 += x1_change # += A += B is equivalent to A = A + B
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1 , y1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.display.update() # telling the display to update with the most current image drawn
    
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed) # set speed of game using snake speed variable to easily make changes
        
    pygame.quit()
    quit()


gameLoop()