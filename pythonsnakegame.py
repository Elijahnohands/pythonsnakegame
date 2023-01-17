import pygame
pygame.init()

dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width,dis_height)) # creates the display and defines its size

pygame.display.set_caption('Snake game by Elijahnohands') # I think this names the window 

blue = (0, 0, 255) # inititalizing colors used 
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
game_over = False #initilizes the game over state

x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
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

    x1 += x1_change # += A += B is equivalent to A = A + B
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1 , y1, 10, 10])

    pygame.display.update() # telling the display to update with the most current image drawn

    clock.tick(30) # set speed of game

pygame.quit()
quit()