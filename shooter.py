import pygame
from pygame.locals import *
from pygame import mixer
from random import randint
pygame.init() # initiate the pygame
gameDisplay = pygame.display.set_mode((720,720)) # screen orientation
pygame.display.set_caption("shooter")  # set the name of the game
clock = pygame.time.Clock()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)      
green = (100,255,130)
x = randint(10,650)
y = 10
p1 = 50
p2 = 620
p3 = 90
p4 = 590
step = 5
score = "score = " 
x_change = 0
y_change = 0
player_score = 0
def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",35)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (70,25)
    gameDisplay.blit(TextSurf, TextRect)
def player():
    message_display(score)
def score_1(count):
    font = pygame.font.Font("freesansbold.ttf",35)
    text = font.render(str(count), True,black)
    gameDisplay.blit(text,(130,10))
def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_4(text):
    largeText = pygame.font.Font("freesansbold.ttf",100)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (360,400)
    gameDisplay.blit(TextSurf, TextRect)
def GameOver ():
    message_4("GAME OVER")
gameOver = False

# add background sound
mixer.init()
mixer.music.load('bensound-summer_ogg_music.ogg')
mixer.music.play()

while not gameOver:
    gameDisplay.fill(white)
    block = pygame.draw.rect(gameDisplay,green,(x,y,50,50))
    boundary = pygame.draw.rect(gameDisplay,black,(0,670,800,300))
    shooter = pygame.draw.rect(gameDisplay,red,(p1,p2,100,50))
    bullet = pygame.draw.rect(gameDisplay,red,(p3,p4,20, 20)) 
    collide = pygame.Rect.colliderect(block,shooter)
    collide_1 = pygame.Rect.colliderect(block,bullet)
    player()
    score_1(player_score)
    y_change = 4
    p4 -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    if player_score > 10: 
        y_change = 5
    if player_score > 20:
        y_change = 6
    if player_score > 30:
        y_change = 8  
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RIGHT]:
        p1 += step
        p3 += step 
    if keys[pygame.K_LEFT]:
        p1 -= step
        p3 -= step
    if y > 620:
        GameOver()
        gameOver = True
    if collide:
        GameOver()
        gameOver = True
    if collide_1:
        x = randint(10,710)
        y = 10 
        player_score += 1
    if p1 < 5:
        p1 += step 
    elif p1 > 615:
        p1 -= step
    if p4 <= 0:
        p4 = 590 
    if x < 5:
        x += step 
    elif x > 615:
        x = 650 
    x += x_change
    y += y_change
    pygame.display.update()
    clock.tick(60)
pygame.quit() # Game ends
quit()                 
