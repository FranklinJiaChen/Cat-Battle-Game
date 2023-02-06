import pygame
import os
from random import randint
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
CUSTOM = (0, 50, 50)
pygame.init()
 
mentronome = 1    # Counter for when to change gif for Orange cat
mentronome2 = 1   # Counter for when to change gif for Grey cat
left = False      # Is orange cat facing left or right?
left2 = False     # Is grey cat facing left or right?
up = True         # Is orange cat Is the tail up or down
up2 = False       # Is grey cat Is the tail up or down
attack = False    # Is the cat attacking?
attack2 = False  
fired = False     # Has the shot been fired
fired2 = False
shotleft = False  # Is the shot fired left or right?
shotleft2 = False
health = 100
health2 = 100
speed = 5
death = False # Is the cat DEAD :(
death2 = False
once = False
once2 = False
height = 650   #height of screen (original is 800*1500) (second is 700*1300)
width = 1100 #width of screen
limit = 0 # How much the border is getting smaller
bordermentronome = 1
x = randint(0,width-100)
y = randint(0,height-100)
x2 = randint(0,width-100)
y2 = randint(0,height-100)
our = pygame.image.load('our.png')
odr = pygame.image.load('odr.png')
oul = pygame.image.load('oul.png')
odl = pygame.image.load('odl.png')
gur = pygame.image.load('gur.png')
gdr = pygame.image.load('gdr.png')
gul = pygame.image.load('gul.png')
gdl = pygame.image.load('gdl.png')
oura = pygame.image.load('oura.png')
odra = pygame.image.load('odra.png')
oula = pygame.image.load('oula.png')
odla = pygame.image.load('odla.png')
gura = pygame.image.load('gura.png')
gdra = pygame.image.load('gdra.png')
gula = pygame.image.load('gula.png')
gdla = pygame.image.load('gdla.png')
oura = pygame.image.load('oura.png')
greenlaser = pygame.image.load('Green Laser.png')
redlaser = pygame.image.load('Red Laser.png')
 
 
 
# Set the width and height of the screen [width, height]
size = (width, height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Cat Battle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(CUSTOM)
 
    # --- Drawing code should go here
    procode = 100 - health2                             #How much damage has Grey Cat Recieved
    if mentronome < 31:                                 #ORANGE cat tail up or down?
        up = True
    else:
        up = False
    if mentronome == 60:
        mentronome -= 59
    else:
        mentronome += 1
 
 
    if mentronome2 < 30:                              #GREY cat tail up or down?                      
        up2 = True
    else:
        up2 = False
    if mentronome2 == 60:                  
        mentronome2 -= 59
    else:
        mentronome2 += 1
 
    if bordermentronome == 59:                                 #Mentronome for border
        limit += 1
    if bordermentronome == 60:
        bordermentronome -= 59
    else:
        bordermentronome += 1
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y>-20+limit:                                #ORANGE cat moving
        y -= speed
    if keys[pygame.K_s] and y<height-130-limit:
        y += speed
    if keys[pygame.K_a] and x>-10+limit:
        x -= speed
        left = True
    if keys[pygame.K_d] and x<width-120-limit:
        x += speed
        left = False
 
 
    if keys[pygame.K_UP]  and y2>-20+limit:                                #GREY cat moving
        y2 -= speed
    if keys[pygame.K_DOWN] and y2< height - 130-limit:
        y2 += speed
    if keys[pygame.K_LEFT] and x2>-10+limit:
        x2 -= speed  
        left2 = True
    if keys[pygame.K_RIGHT] and x2<width-120-limit:
        x2 += speed
        left2 = False
 
   
    if not keys[pygame.K_RETURN]:
       attack2 = False
 
    if fired == False and left == True and up == True:           # Orange cats lasers
        glaserx = x+29
        glasery = y+60
        shotleft = True
    if fired == False and left == True and up == False:
        glaserx = x+25
        glasery = y+61
        shotleft = True
    if fired == False and left == False and up == True:
        glaserx = x+82
        glasery = y+60
        shotleft = False
    if fired == False and left == False and up == False:
        glaserx = x+86
        glasery = y+61
        shotleft = False
    if fired == True and shotleft == False:
        screen.blit(greenlaser, [glaserx,glasery])
        glaserx +=10
    if fired == True and shotleft == True:
        screen.blit(greenlaser, [glaserx,glasery])
        glaserx -=10
    if glaserx < limit or glaserx > width - limit:
        fired = False
 
 
 
 
    if fired2 == False and left2 == True and up2 == True:            #Grey cats lasers
        rlaserx = x2+29
        rlasery = y2+60
        shotleft2 = True
    if fired2 == False and left2 == True and up2 == False:
        rlaserx = x2+25
        rlasery = y2+61
        shotleft2 = True
    if fired2 == False and left2 == False and up2 == True:
        rlaserx = x2+82
        rlasery = y2+60
        shotleft2 = False
    if fired2 == False and left2 == False and up2 == False:
        rlaserx = x2+86
        rlasery = y2+61
        shotleft2 = False
    if fired2 == True and shotleft2 == False:
        screen.blit(redlaser, [rlaserx,rlasery])
        rlaserx +=10
    if fired2 == True and shotleft2 == True:
        screen.blit(redlaser, [rlaserx,rlasery])
        rlaserx -=10
    if rlaserx < limit or rlaserx > width - limit:
        fired2 = False
 
 
# Hitboxes
    rlaserhb = pygame.Rect (rlaserx, rlasery, 15, 1)
    glaserhb = pygame.Rect (glaserx, glasery, 15, 1)
    ourheadhb = pygame.Rect (x+67, y+32, 32, 38)
    odrheadhb = pygame.Rect (x+71, y+32, 32, 36)
    gurheadhb = pygame.Rect (x2+67, y2+32, 32, 38)
    gdrheadhb = pygame.Rect (x2+71, y2+32, 32, 36)
    oulheadhb = pygame.Rect (x+29, y+32, 32, 38)
    odlheadhb = pygame.Rect (x+25, y+33, 32, 36)
    gulheadhb = pygame.Rect (x2+29, y2+32, 32, 38)
    gdlheadhb = pygame.Rect (x2+25, y2+33, 32, 36)
 
    ourbodyhb = pygame.Rect (x+47, y+70, 52, 20)
    odrbodyhb = pygame.Rect (x+51, y+69, 52, 20)
    gurbodyhb = pygame.Rect (x2+47, y2+70, 52, 20)
    gdrbodyhb = pygame.Rect (x2+51, y2+69, 52, 20)
    oulbodyhb = pygame.Rect (x+29, y+72, 52, 20)
    odlbodyhb = pygame.Rect (x+25, y+69, 52, 20)
    gulbodyhb = pygame.Rect (x2+29, y2+72, 52, 20)
    gdlbodyhb = pygame.Rect (x2+25, y2+69, 52, 20)
    leftborderhb = (0, 0 , limit, height-20) # left
    topborderhb = (0, 0 , width, limit) # top
    bottomborderhb = (0, height - 20 - limit, width, 1000) # bottom
    rightborderhb = (width-limit, 0, 1000, height) # right
 
 
    if rlaserhb.colliderect(ourheadhb) and fired2 == True and up == True and left == False and death == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat headshots Orange Cat")
    if rlaserhb.colliderect(odrheadhb) and fired2 == True and up == False and left == False and death == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat headshots Orange Cat")
    if glaserhb.colliderect(gurheadhb) and fired == True and up2 == True and left2 == False and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat headshots Grey Cat")
    if glaserhb.colliderect(gdrheadhb) and fired == True and up2 == False and left2 == False and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat headshots Grey Cat")
    if rlaserhb.colliderect(oulheadhb) and fired2 == True and up == True and left == True and death == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat headshots Orange Cat")
    if rlaserhb.colliderect(odlheadhb) and fired2 == True and up == False and left == True and death == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat headshots Orange Cat")
    if glaserhb.colliderect(gulheadhb) and fired == True and up2 == True and left2 == True and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat headshots Grey Cat")
    if glaserhb.colliderect(gdlheadhb) and fired == True and up2 == False and left2 == True and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat headshots Grey Cat")
 
    if rlaserhb.colliderect(ourbodyhb) and fired2 == True and up == True and left == False and death2 == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat hits Orange Cat's body")
    if rlaserhb.colliderect(odrbodyhb) and fired2 == True and up == False and left == False and death2 == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat hits Orange Cat's body")
    if glaserhb.colliderect(gurbodyhb) and fired == True and up2 == True and left2 == False and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat hits Grey Cat's body")
    if glaserhb.colliderect(gdrbodyhb) and fired == True and up2 == False and left2 == False and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat hits Grey Cat's body")
    if rlaserhb.colliderect(oulbodyhb) and fired2 == True and up == True and left == True and death == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat hits Orange Cat's body")
    if rlaserhb.colliderect(odlbodyhb) and fired2 == True and up == False and left == True and death == False:
        health -= 4
        rlaserx = -1000
        rlasery = -1000
        print ("Grey Cat hits Orange Cat's body")
    if glaserhb.colliderect(gulbodyhb) and fired == True and up2 == True and left2 == True and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat hits Grey Cat's body")
    if glaserhb.colliderect(gdlbodyhb) and fired == True and up2 == False and left2 == True and death2 == False:
        health2 -= 4
        glaserx = -1000
        glasery = -1000
        print ("Orange Cat hits Grey Cat's body")
 
    if rlaserhb.colliderect(leftborderhb):
        rlaserx = -1000
        rlasery = -1000
        fired2 == False
    if rlaserhb.colliderect(rightborderhb):
        rlaserx = -1000
        rlasery = -1000
        fired2 == False
    if glaserhb.colliderect(leftborderhb):
        glaserx = -1000
        glasery = -1000
        fired == False
    if glaserhb.colliderect(rightborderhb):
        glaserx = -1000
        glasery = -1000
        fired == False
 
    pygame.draw.rect(screen, PURPLE, [0, 0 , limit, height-20]) # left border
    pygame.draw.rect(screen, PURPLE, [0, 0 , width, limit]) # top border
    pygame.draw.rect(screen, PURPLE, [0, height - 20 - limit, width, 1000]) # bottom border
    pygame.draw.rect(screen, PURPLE, [width-limit, 0, 1000, height]) # right border
    pygame.draw.rect(screen, BLACK, [0, height - 21, width, 21])
    pygame.draw.rect(screen, RED, [-1, height-20, health * width/200, 20])      # Health Bar           (-1,height-20,health*width/200,20)
    pygame.draw.rect(screen, GREEN, [width/2+procode * width/200, height-20, width/2, 20])                     #(width/2+procode * 7.5,height-20,height-20,20)
    if health < 1 and once == False:
        death = True
        print ("Orange Cat got rekt")
        once = True
    if health2 < 1 and once2 == False:
        death2 = True
        print ("Grey Cat got rekt")
        once2 = True
 
    if up == True and left == True and attack == False and death == False:                     #ORANGE which cat is getting displayed
        screen.blit(oul, [x,y])
    elif up == True and left == False and attack == False and death == False:
        screen.blit(our, [x,y])
    elif up == False and left == True and attack == False and death == False:
        screen.blit(odl, [x,y])
    elif attack == False and death == False:
        screen.blit(odr, [x,y])
 
 
    if up2 == True and left2 == True and attack2 == False and death2 == False:                     #GREY which cat is getting displayed
        screen.blit(gul, [x2,y2])
    elif up2 == True and left2 == False and attack2 == False and death2 == False:
        screen.blit(gur, [x2,y2])
    elif up2 == False and left2 == True and attack2 == False and death2 == False:
        screen.blit(gdl, [x2,y2])
    elif attack2 == False and death2 == False:
        screen.blit(gdr, [x2,y2])
    if keys[pygame.K_SPACE] and up == True and left == True and glaserx < width and glaserx > 0 and death == False:       #Orange cats firing
        fired = True
        screen.blit(oula, [x,y])
        attack = True
    if keys[pygame.K_SPACE] and up == True and left == False and glaserx < width and glaserx > 0 and death == False:
        fired = True
        screen.blit(oura, [x,y])
        attack = True
    if keys[pygame.K_SPACE] and up == False and left == True and glaserx < width and glaserx > 0 and death == False:
        fired = True
        screen.blit(odla, [x,y])
        attack = True
    if keys[pygame.K_SPACE] and up == False and left == False and glaserx < width and glaserx > 0 and death == False:
        fired = True
        screen.blit(odra, [x,y])
        attack = True
 
    if not keys[pygame.K_SPACE]:
        attack = False
    if keys[pygame.K_RETURN] and up2 == True and left2 == True and rlaserx < width and rlaserx > 0 and death2 == False:       #Grey cats firing
        fired2 = True
        screen.blit(gula, [x2,y2])
        attack2 = True
    if keys[pygame.K_RETURN] and up2 == True and left2 == False and rlaserx < width and rlaserx > 0 and death2 == False:
        fired2 = True
        screen.blit(gura, [x2,y2])
        attack2 = True
    if keys[pygame.K_RETURN] and up2 == False and left2 == True and rlaserx < width and rlaserx > 0 and death2 == False:
        fired2 = True
        screen.blit(gdla, [x2,y2])
        attack2 = True
    if keys[pygame.K_RETURN] and up2 == False and left2 == False and rlaserx < width and rlaserx > 0 and death2 == False:
        fired2 = True
        screen.blit(gdra, [x2,y2])
        attack2 = True
 
 
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
