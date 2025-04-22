import pygame ,sys
import random
import math
from pygame import mixer

pygame.init()

vel=0.1
vell=0.5

# create the screen
win=pygame.display.set_mode((800,600))

#background and music
background=pygame.image.load('back.jpg')

mixer.music.load('backmusic.mp3')
mixer.music.play(-1)
#title and icon
pygame.display.set_caption('dogsfordogs')
icon=pygame.image.load('dog1.png')
pygame.display.set_icon(icon)

#player dog

dogImg=pygame.image.load('belkaa.png')
dogx=300
dogy=300

#player cat
y1=random.randint(0,200)
y2=random.randint(380,580)
catImg=pygame.image.load('cat.png')
catx=random.randint(0,750)
caty=random.choice([y1,y2])

#pet food
petFoodImg=pygame.image.load('petFood.png')
petx=400
pety=300

def dogD(x,y):
    win.blit(dogImg,(x,y))

a=0
b=0

def iscollision(catx,caty,dogx,dogy):
    distance=math.sqrt((math.pow(catx-dogx,2))+(math.pow(caty-dogy,2)))
    if distance<27:
        return True
    else:
        return False

def catD(x,y):
    win.blit(catImg,(x,y))

scorevaleu1=3
scorevaleu=scorevaleu1
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
numlevel1=0
numlevel=numlevel1

def show(x,y):
    score=font.render('cat : '+str(scorevaleu),True,(255,255,255))
    win.blit(score,(x,y))

def level(x,y):
    level=font.render('level : '+str(numlevel),True,(255,255,255))
    win.blit(level,(x,y))

def gameover():
    time.sleep(3)
    pygame.quit()
    quit
myfont1=pygame.font.SysFont('aakar',30,bold=5)
myfont2=pygame.font.SysFont('aakar',60,bold=10)
color1=(0,255,0)
color2=(255,0,0)
fcolor1=(0,0,0)
fcolor2=(255,255,255)

is_menu=True
def cleaner():
    global is_menu,two_menu
    is_menu=False
    two_menu=False
    
P='Play'
Q='Quit'
L='Lets Play Game'
x1=225
    
def change():
    global is_menu ,P ,L ,x1
    is_menu=True
    x1=300
    P='Next'
    L='You win'
    
two_menu=False
def changecat():
    global two_menu ,P ,L
    two_menu=True
    P='Again'
    L='Game Over'
    scorevaleu=scorevaleu1
    
while True:

    win.blit(background,(a,b))
    if a>-2200:
        a-=0.03

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if is_menu:
        if event.type==pygame.MOUSEBUTTONDOWN :
            mouse1=pygame.mouse.get_pos()
            if (150<mouse1[0]<350 and 350<mouse1[1]<430):
                cleaner()
                vel+=0.05
                scorevaleu1+=2
                scorevaleu=scorevaleu1
                numlevel1+=1
                numlevel=numlevel1
            if (450<mouse1[0]<650 and 350<mouse1[1]<430):
                pygame.quit()
                quit
                
    if two_menu:
        if event.type==pygame.MOUSEBUTTONDOWN :
            mouse1=pygame.mouse.get_pos()
            if (150<mouse1[0]<350 and 350<mouse1[1]<430):
                cleaner()
                catx=random.randint(0,750)
                y1=random.randint(0,150)
                y2=random.randint(380,580)
                caty=random.choice([y1,y2])
                scorevaleu=scorevaleu1
            if (450<mouse1[0]<650 and 350<mouse1[1]<430):
                pygame.quit()
                quit
    
    if is_menu :        
        renderp=myfont1.render(P+'!',True,(fcolor1))
        renderq=myfont1.render(Q+'!',True,(fcolor1))
        rendert=myfont2.render(L+'!',True,(fcolor2))
        pygame.draw.rect(win,(color1),(150,350,200,80))
        pygame.draw.rect(win,(color2),(450,350,200,80))
        win.blit(rendert,(x1,100))
        win.blit(renderp,(220,380))
        win.blit(renderq,(530,380))

    if two_menu :        
        renderp=myfont1.render(P+'!',True,(fcolor1))
        renderq=myfont1.render(Q+'!',True,(fcolor1))
        rendert=myfont2.render(L+'!',True,(fcolor2))
        pygame.draw.rect(win,(color1),(150,350,200,80))
        pygame.draw.rect(win,(color2),(450,350,200,80))
        win.blit(rendert,(250,100))
        win.blit(renderp,(220,380))
        win.blit(renderq,(530,380))
    
    if (not is_menu)and(not two_menu) :       
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse=pygame.mouse.get_pos()
                
            if (dogx <mouse[0]<dogx+60) and (dogy<mouse[1]<dogy+60):
                dogsound=mixer.Sound('doogsound.mp3')
                dogsound.play()
            if (catx <mouse[0]<catx+60) and (caty<mouse[1]<caty+60):
                dogsound=mixer.Sound('catsound.mp3')
                dogsound.play()

                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dogx>0:
            dogx -= vell
        if keys[pygame.K_RIGHT] and dogx<800-62:
            dogx += vell
        if keys[pygame.K_UP] and dogy>0:
            dogy -= vell 
        if keys[pygame.K_DOWN] and dogy<600-65:
            dogy += vell
            
        if (dogx==0.5 and 600>dogy>0) or (dogx==737.5 and 600>dogy>0)or (dogy==0.5 and 800>dogx>0)or (dogy==534.5 and 600>dogy>0):
            dogsound=mixer.Sound('doggsound.mp3')
            dogsound.play()
            
        if catx>380 and catx !=380 :
            catx-=vel
        if catx<380 and catx !=380 :
            catx+=vel
        if caty>250 and caty !=250 :
            caty-=vel
        if caty<250 and caty !=250 :
            caty+=vel
            
        catD(catx,caty)

        collision=iscollision(catx,caty,dogx,dogy)
        if collision:
            catx=random.randint(0,750)
            y1=random.randint(0,130)
            y2=random.randint(380,580)
            caty=random.choice([y1,y2])
            scorevaleu-=1
            dogsound=mixer.Sound('doggsound.mp3')
            dogsound.play()
            
        dogD(dogx,dogy)  
        show(textx,texty)
        level(650,10)
        win.blit(petFoodImg,(petx,pety))

    if scorevaleu==0:
        change()
    
    if 245<caty<255 and 375<catx<395:
        changecat()
    
    pygame.display.update()


