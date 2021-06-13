import math
import pygame
import sys
from pygame.locals import *
import os

maxN = 1000
zoom = 0.7
centerx=960
centery=480

#pygame Init
pygame.init();#display init
size=width,height=1920,1080
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Fourier")
clock=pygame.time.Clock()
FPS=2400
BackColor=(255,255,255)
print('Pygame Init Finished')

FONT = pygame.font.Font('C:\WINDOWS\FONTS\SIMSUN.TTC', 48) #Font & Size

#Import Input-Vectors
fp=open(r'E:\游戏\FourierCircleDrawing\FourierCircleDrawing\FourierCircleDrawing\FourierMath\MIKUC_datas_2000000.txt')
xy=[]
n=0
x=[];
y=[];
for line in fp:
    if n > maxN:
        break
    xy=eval(line.strip())
    x.append(xy[0])
    y.append(xy[1])
    n += 1
print('Import Input-Vectors Finished')

x[0]=0
y[0]=0

length = len(x);
r=[]
w=[]
for n in range(0,length):
    r.append(math.sqrt(x[n]**2+y[n]**2))
    w.append(math.floor(n/2+0.5)*((-1) if (n%2==0) else 1))
    
def CalcuPoint(intime):
    ansx=0
    ansy=0
    for n in range(0,length):
        alpha = w[n]*t
        c = math.cos(alpha)
        s = math.sin(alpha)
        dx = x[n]*c-y[n]*s
        dy = x[n]*s+y[n]*c
        #circle
        #line
        ansx += dx
        ansy += dy
    return (ansx*zoom+centerx,ansy*zoom+centery)

t = 0
dt = 0.0001*math.pi*2
trick = [CalcuPoint(0)]
endt = 10
while t<=endt:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False;
            pygame.quit();
    out=CalcuPoint(t)
    trick.append(out)
    t += dt
    screen.fill(BackColor)#clearbroad
    pygame.draw.lines(screen,(0x39,0xc5,0xbb),False,trick,2)#drawtrick
    pygame.display.set_caption('t='+str(round(t,9)))
    text_surface=FONT.render('t='+str(round(t,9)),1,(0x39,0xc5,0xbb))
    screen.blit(text_surface,(0,0))
    pygame.display.flip();
    clock.tick(FPS);
os.system('pause')
