import pygame , sys
from pygame.locals import *
pygame.init()
#---(Define variables)-------------------------------------------
counter = 0
height = 600
width = 800
cat_x = 380
cat_y = 320
cat_w=80
cat_h=80
cat_s=10
speed=3

par1_x=800
par1_y=100
par2_x=1200
par2_y=200
par3_x=-300
par3_y=150
par4_x=-800
par4_y=50
speed_par=0.3

#---(surface and background)-------------------------------------------
win=pygame.display.set_mode((width, height))
pygame.display.set_caption("Mahdavi Yar")
bg=pygame.image.load("a1.jpg")
BG=pygame.transform.scale(bg,(width,height))

#---(Cat & butterflies)-------------------------------------------
while True:
    char=pygame.image.load("cat.png")
    CHAR=pygame.transform.scale(char,(cat_w,cat_h))
    win.blit(BG,(0,0))
    win.blit(CHAR,(cat_x,cat_y))

    par1=pygame.image.load("parv1.png")
    PAR1=pygame.transform.scale(par1,(50,50))
    win.blit(PAR1,(par1_x,par1_y))

    par2=pygame.image.load("parv2.png")
    PAR2=pygame.transform.scale(par2,(50,50))
    win.blit(PAR2,(par2_x,par2_y))

    par3=pygame.image.load("parv3.png")
    PAR3=pygame.transform.scale(par3,(50,50))
    win.blit(PAR3,(par3_x,par3_y))

    par4=pygame.image.load("parv4.png")
    PAR4=pygame.transform.scale(par4,(50,50))
    win.blit(PAR4,(par4_x,par4_y))

#---(Exit & Cat voice)---------------------------------------------
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                crash_sound = pygame.mixer.Sound("miaoo.wav")
                pygame.mixer.Sound.play(crash_sound)
    
#---(Moving the cat with the keyboard )---------------------------------------------                    
    if event.type==KEYDOWN:
        if event.key==K_DOWN:
            cat_y+=speed
                       
        if event.key==K_UP:
            cat_y-=speed
            
        if event.key==K_RIGHT:
            cat_x+=speed
            
        if event.key==K_LEFT:
            cat_x-=speed
            
#---(Hunting butterflies and displaying its icon )--------------------------------------------
    if (par1_x > -80):
        par1_x -= speed_par+0.1
        if abs(par1_x-cat_x)<=50 and abs(par1_y-cat_y)<=30:
            par1_x=-50
            counter+=1
   
        p1=pygame.image.load("p1.png")
        P1=pygame.transform.scale(p1,(35,35))
        win.blit(P1,(740,15))

    if (par2_x > -80):
        par2_x -= speed_par+0.3
        if abs(par2_x-cat_x)<=50 and abs(par2_y-cat_y)<=30:
            par2_x=-50
            counter+=1
        p2=pygame.image.load("p2.png")
        P2=pygame.transform.scale(p2,(35,35))
        win.blit(P2,(700,15))

    if (par3_x < 850):
        par3_x += speed_par+0.4
        if abs(par3_x-cat_x)<=50 and abs(par3_y-cat_y)<=30:
            par3_x=850
            counter+=1
        p3=pygame.image.load("p3.png")
        P3=pygame.transform.scale(p3,(35,35))
        win.blit(P3,(660,15))
                
    if (par4_x < 850):
        par4_x += speed_par+0.2
        if abs(par4_x-cat_x)<=50 and abs(par4_y-cat_y)<=30:
            par4_x=850
            counter+=1
        p4=pygame.image.load("p4.png")
        P4=pygame.transform.scale(p4,(35,35))
        win.blit(P4,(620,15))

#---(The message of victory or Game Over)---------------------------------------                
    if (par4_x>800):
        if (counter==4) :
            text_win="Victory"
            font = pygame.font.Font(None, 30)
            t_s_w = font.render(text_win, True, (255, 255, 0))
            t_r_w = t_s_w.get_rect()
            t_r_w.center = (570, 35)
            win.blit(t_s_w, t_r_w)
            cat_x = 380
            cat_y = 320
            
        elif (counter<4):
            text_ovr="Game Over"
            font = pygame.font.Font(None, 25)
            t_s_o = font.render(text_ovr, True, (255, 255, 0))
            t_r_o = t_s_o.get_rect()
            t_r_o.center = (575, 35)
            win.blit(t_s_o, t_r_o)
            cat_x = 380
            cat_y = 320
    
#---(update pygame)--------------------------------------------
    pygame.display.update()
