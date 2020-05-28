#1Packages
import pygame
import math
import random
from pygame.locals import *

####2
#    Variables
####
pygame.init()
width,height = 640,480
gameWindow = pygame.display.set_mode((width,height))
keys = [False,False]
playerPosition = [100,100]
castlePositions = [ (100,30), (100,135), (100,240), (100,345) ]
badgerPositions = [ (640,30),(640,135),(640,240),(640,345) ]
flag = 0
acc = [0,0]
arrows = []
badtimer = 100
badtimer1 = 0
badguys = [[640,480]]
healthvalue = 194

# 3 Load assets
fighter = pygame.image.load("assets/images/dude.png")
grass = pygame.image.load("assets/images/grass.png")
castle = pygame.image.load("assets/images/castle.png")
arrow = pygame.image.load("assets/images/bullet.png")
badguyimg1 = pygame.image.load("assets/images/badguy.png")
badguyimg = badguyimg1

## 4 game starts here

running = 1
while running:
	badtimer-=1
	#5
	gameWindow.fill(0)
	#6
	for x in range(int(width/grass.get_width()+1)):
		for y in range(int(height/grass.get_height()+1)):
			gameWindow.blit(grass,(x*100,y*100))
	gameWindow.blit(castle,(0,30))
	gameWindow.blit(castle,(0,135))
	gameWindow.blit(castle,(0,240))
	gameWindow.blit(castle,(0,345))
	gameWindow.blit(fighter,playerPosition)

	#6.2 firing arrows
	for bullet in arrows:
		index=0
		# velx=math.cos(bullet[0])*10
		# vely=math.sin(bullet[0])*10
		bullet[0]+=10
		bullet[1]+=10
		if bullet[1]<-64 or bullet[1]>640 or bullet[0]<-64 or bullet[0]>480:
			arrows.pop(index)
		index+=1
		for projectile in arrows:
			# arrow1 = pygame.transform.rotate(arrow,360-projectile[0]*57.29)
			# arrow1 = pygame.transform.rotate(arrow,360)
			gameWindow.blit(arrow,(projectile[0],projectile[1]))


	#6.3 drawing enemies
	if badtimer == 0:
		badguys.append(list(random.choice(badgerPositions)))
		badtimer = 100 - (badtimer1*2)
		if badtimer1>=35:
			badtimer1=35
		else:
			badtimer1+=5
	index = 0
	for badguy in badguys:
		if badguy[0]<-64:
			badguys.pop(index)
		badguy[0]-=7
		#6.3.1 - Attack castle
		badrect=pygame.Rect(badguyimg.get_rect())
		badrect.top=badguy[1]
		badrect.left=badguy[0]
		if badrect.left<64:
			healthvalue -= random.randint(5,20)
			badguys.pop(index)
        # 6.3.3 - Next bad guy
		index+=1
	for badguy in badguys:
		gameWindow.blit(badguyimg,badguy)

	#7
	pygame.display.flip()
	#8
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key ==K_s:
				#keys[0] = True
				if flag in range(3):
					flag+=1
			elif event.key == K_w:
				#keys[1] = True
				if flag in range(1,4):
					flag-=1
			elif event.key == K_RIGHT or event.key == K_LEFT:
				acc[1]+=1
				arrows.append([playerPosition])
	if flag in range(4):
		playerPosition = castlePositions[flag]
