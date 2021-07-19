import pygame
import math
from math import sqrt
import random
# Renkleri tanimlama
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE=(0,134,250)
PINK=(255,0,198)
 
# Gridlerin yükseklik ve genisliklerini ayarlama
WIDTH = 50
HEIGHT = 50
 
# Gridler arasi bosluk ayarlanma
MARGIN = 5
 
# Grid yaopisi olusturuluyor
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
Q=[] #q tablosu olusturuluyor 
for i in range(0,10):
    Q.append([])
    for r in range(0,10):
        Q[i].append([0,0,0,0])#sol,sag,yukari,assagi

#gridlerin ilk baslangic noktasi 0,0 bitis noktasi 9,9 olarak belirlendigi icin renk kodlari ataniyor
grid[0][0] = 1
grid[9][9] = 2
# Initialize pygame
pygame.init()
 
# ekran boyutlari ayarlaniyor
WINDOW_SIZE = [555, 555]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Indiana Jones - Hazine Arayışında")
 
done = False
 
clock = pygame.time.Clock()

start=0
uu=0
X=0
Y=0
finish=0
sayac=0
sayac2=0
greedy=0.8
LP=-10 #Living Penalty
ogr=0.1 #ogrenme orani
A=0.9#discount rate
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN and start !=1:
            
            pos = pygame.mouse.get_pos()
           
            column = pos[0] // (WIDTH + MARGIN) #mouse evetinden gelen degerleri grid karsiligini hesaplama
            row = pos[1] // (HEIGHT + MARGIN)
            
            if(grid[row][column]==1):#oyuna baslayip baslamadigina bakiyor (0,0 inci grid tiklanmis mi?)
                start=1
                R=[]
                for row in range(10):
                    R.append([])
                    for column in range(10):
                        R[row].append(0)
                        
                for y in range(0,10):
                    for x in range(0,10):
                        R[y][x]= sqrt((0-y)**2+(0-x)**2)*3#oklid uzaklik alindi
                        #R[y][x]=-1
                        if y==9 and x==9:
                            R[i][r]=10000000000000 #hedef nokta

                #-------------------------------------------------
                        
                #Enviroment tanimlanmis engeller Q-tableye ekleniyor
                for i in range(0,10):
                    for r in range(0,10):
                        if grid[i][r]==3:
                            R[i][r]="N"

                for y in range(0,10):#soldan ---> saga gidiyor
                    for x in range(0,10):
                        if R[y][x]=="N" and x>0:
                            Q[y][x-1][1]=-99999999999 #sag gitme aktionunu aldi
                        if x==9:
                            Q[y][x][1]=-99999999999

                for y in range(0,10):#sagdan <--- sola gidiyor
                    for x in range(9,-1,-1):
                        if R[y][x]=="N" and x<9:#sola gitme aksiyonu
                            Q[y][x+1][0]=-99999999999
                        if x==0:
                            Q[y][x][0]=-99999999999

                for x in range(0,10): #yukaridan assagi gitmek
                    for y in range(0,10):
                        if R[y][x]=="N" and y>0: #asagi gitme aksiyonu
                            Q[y-1][x][3]=-99999999999
                        if y==9:
                            Q[y][x][3]=-99999999999

                for x in range(0,10): #assgidan yukari dogru
                    for y in range(9,-1,-1):
                        if R[y][x]=="N" and y<9: #yukari gitme aksiyonu
                            Q[y+1][x][2]=-99999999999
                        if y==0:
                            Q[y][x][2]=-99999999999
                
                #--------------------------------------------------                            
            if(grid[row][column]==0):
                grid[row][column] = 3
            elif(grid[row][column]==3):
                grid[row][column] = 0
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
    sayac=sayac+1
    # --------  Q learning egitim kısmı 
    #basladigin state grid[0][0] == R[0][0]
    if (start==1 and finish==0):
    
        print ("****")
        s=random.random()
        #print (s)
        if(s<greedy):
            t=0
            while t==0:
                randomsayi=random.randint(0,3)
                if(Q[Y][X][randomsayi]==-99999999999):
                    t=0
                else:
                    #maxaction=Q[Y][X][randomsayi]
                    maxactionindex=randomsayi
                    t=1
        else:
            maxaction=max(Q[Y][X])
            maxactionindex=Q[Y][X].index(maxaction)
        if(maxactionindex == 0 ):#sol hareket
            print (Y,"-",X," >> durumunda = ","sol hareket etti")
            Q[Y][X][0]=Q[Y][X][0]+ogr*(R[Y][X-1]+A*max(Q[Y][X-1])-Q[Y][X][0])+LP
            X=X-1
        if(maxactionindex == 1 ):#SAG hareket
            print (Y,"-",X," >> durumunda = ","sag hareket etti")
            Q[Y][X][1]=Q[Y][X][1]+ogr*(R[Y][X+1]+A*max(Q[Y][X+1])-Q[Y][X][1])+LP
            X=X+1
        if(maxactionindex == 2 ):#YUKARI hareket
            print (Y,"-",X," >> durumunda = ","yukari hareket etti")
            Q[Y][X][2]=Q[Y][X][2]+ogr*(R[Y-1][X]+A*max(Q[Y-1][X])-Q[Y][X][2])+LP
            Y=Y-1
        if(maxactionindex == 3 ):#ASAGI hareket
            print (Y,"-",X," >> durumunda = ","asaga hareket etti")
            Q[Y][X][3]=Q[Y][X][3]+ogr*(R[Y+1][X]+A*max(Q[Y+1][X])-Q[Y][X][3])+LP
            Y=Y+1


        grid[Y][X] = 4
        #print (sayac,"************************************************")
        if sayac>100:
            sayac2=sayac2+1
            greedy=0.8*math.exp(-sayac2/100.0) #gredy kucultme
            sayac=0
            uu=1
        if (X==9 and Y==9) or uu==1:
            sayac=0
            X=0
            Y=0
            for row in range(10):
                for column in range(10):
                    if(grid[row][column] == 4):
                        grid[row][column] = 0
            
            grid[9][9]=2
            grid[0][0]=1
            #print ("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
            sayac2=sayac2+1
            greedy=0.8*math.exp(-sayac2/100.0)
            uu=0
        
    #
    # Draw the grid
    for row in range(10):
        for column in range(10):
            if grid[row][column] == 0:#temel alan rengi
                color = WHITE
            if grid[row][column] == 1:#giris noktasi rengi
                color = GREEN
            if grid[row][column] == 2:#cikis noktasi rengi
                color = RED
            if grid[row][column] == 3:#engellerin rengi
                color=BLUE
            if grid[row][column] == 4:#agent hareket rengi
                color=PINK

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    #guncelleme hizi
    clock.tick(20)
 
    #cizilenleri ekrana basma
    pygame.display.flip()
 

pygame.quit()
