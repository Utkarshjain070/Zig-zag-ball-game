import pygame
import random
import time

from pygame.constants import K_UP, KEYDOWN, QUIT

pygame.init()
pygame.mixer.init()


green=(173, 245, 66)
red=(245, 72, 66)
blue=(15, 12, 176)
white=(255,255,255)
black=(0,0,0)
pink=(245, 66, 209)

screen=pygame.display.set_mode((750,550))
pygame.display.set_caption("Zig-Zag Ball with Utkarsh")


def gameover():
    pygame.mixer.music.load('game over music.mp3')
    pygame.mixer.music.play()
    g_exit=False
    while not g_exit:

        g_screen=pygame.display.set_mode((750,550))
        g_screen.fill(green)
        font=pygame.font.SysFont('none',40)
        t1=font.render('Game Over',True,black)
        t2=font.render('Press enter to play',True,black)
        t3=font.render('Press Space to exit',True,black)
        screen.blit(t1,(280,150))
        screen.blit(t2,(230,220))
        screen.blit(t3,(230,270))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                g_exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.mixer.music.load('enter.mp3')
                    pygame.mixer.music.play()
                    game()

                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('enter.mp3')
                    pygame.mixer.music.play()
                    g_exit=True
    pygame.quit()
    quit()



def welcome():
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()
    w_exit=False
    while not w_exit:
    
        w_screen=pygame.display.set_mode((750,550))
        w_screen.fill(green)
        font=pygame.font.SysFont('none',40)
        t1=font.render('Welcome to zig-zag ball with utkarsh',True,black)
        t2=font.render('Press enter to play',True,black)
        screen.blit(t1,(100,150))
        screen.blit(t2,(230,250))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                w_exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.mixer.music.load('enter.mp3')
                    pygame.mixer.music.play()
                    game()
    pygame.quit()
    quit()
    
def game():

    exit=False
    ball_x=random.randint(100,700)
    ball_y=random.randint(100,400)

    vel_x=0.08
    vel_y=0.08

    hand_y=0

    pygame.mixer.music.load('game.mp3')
    pygame.mixer.music.play()
    while not exit:

        screen.fill(red)
        ball=pygame.draw.circle(screen,black,(ball_x,ball_y),10)
        pygame.draw.rect(screen,blue,(0,0,750,9))
        pygame.draw.rect(screen,blue,(0,541,750,9))
        hand=pygame.draw.rect(screen,blue,(740,hand_y,10,90))
        hand=pygame.draw.rect(screen,blue,(0,hand_y,10,90))
        pygame.display.update()
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    hand_y-=50
                if event.key==pygame.K_DOWN:
                    hand_y+=50 


                

        ball_x+=vel_x
        ball_y+=vel_y


        if ball_x>10 and ball_x<=740 and ball_y>10 and ball_y<540:
            ball_x+=vel_x
            ball_y+=vel_y

        if ball_y<=15:

            vel_y=-vel_y
        if ball_y>=535:

            vel_y=-vel_y
        if ball_x<=10:
            pygame.mixer.music.load('game over effect.mp3')
            pygame.mixer.music.play()
            gameover()
        if ball_x>740:
            pygame.mixer.music.load('game over effect.mp3')
            pygame.mixer.music.play()
            gameover()
        if abs(abs(ball_y)-abs(hand_y))<90 and ball_x>730 and ball_y>=hand_y:

            vel_x=-vel_x
        if abs(abs(ball_y)-abs(hand_y))<90 and ball_x<20 and ball_y>=hand_y:

            vel_x=-vel_x
    pygame.quit()
    quit()

welcome()

            
        
      
    

    

