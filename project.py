#importing modules
import pygame as p
import math as m
import random as r

#intializing pygame
p.init()

#game window
screen=p.display.set_mode((1200,1000))

#title and icon
p.display.set_caption("SPACE INVADERS")
icon=p.image.load("C:/Users/Johnny Fernando/Desktop/SPACE INVADERS/space-game.png")
p.display.set_icon(icon)

#background
bg=p.image.load("C:/Users/Johnny Fernando/Desktop/SPACE INVADERS/space.jpg")
def background():
    screen.blit(bg,(0,0))

#player
hero=p.image.load("C:/Users/Johnny Fernando/Desktop/SPACE INVADERS/spaceship.png")
p_xcoord=550
p_ycoord=800
p_xchange=0
def player(x,y):
    screen.blit(hero,(x,y))

#enemy
villain=p.image.load("C:/Users/Johnny Fernando/Desktop/SPACE INVADERS/invaders.png")
v_xcoord=r.randint(0,1200)
v_ycoord=r.randint(100,300)
v_xchange=2
v_ychange=60
def enemy(x,y):
    screen.blit(villain,(x,y))

#bullet
bullet=p.image.load("C:/Users/Johnny Fernando/Desktop/SPACE INVADERS/bullet.png")
l_xcoord=0
l_ycoord=800
l_xchange=0
l_ychange=18
l_state="ready" 
def fire_bullet(x,y):
    global l_state
    l_state = "fire"
    screen.blit(bullet,(x+32,y+20))
    
    
    
#gameloop
run=True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run==False

    #players movement 
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                p_xchange = -3
            if event.key == p.K_RIGHT:
                p_xchange = 3
            if event.key == p.K_SPACE:
                print("Space is pressed")
                l_xcoord = p_xcoord
                fire_bullet(l_xcoord,l_ycoord)
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT or event.key == p.K_RIGHT:
                p_xchange = 0
    p_xcoord += p_xchange         


    background()
    
    #adding borders to ensure spaceship stays inside window
    if p_xcoord <=0:
        p_xcoord = 0
    elif p_xcoord >= 1072:
        p_xcoord = 1072
        
    #enemy movement
    v_xcoord += v_xchange
    
    if v_xcoord <=0:
        v_xchange = 2
        v_ycoord += v_ychange 
    elif v_xcoord >= 1072:
        v_xchange = -2
        v_ycoord += v_ychange

    #bullet movement
        if l_state == "fire":
            fire_bullet(l_xcoord,l_ycoord)
            l_ycoord -= l_ychange
        
    player(p_xcoord,p_ycoord)
    enemy(v_xcoord,v_ycoord)
    p.display.update()
quit()
