#!/usr/bin/python
import pygame
import sys
from pygame.locals import *
import numpy as np
import math

G= 6.67*10**-11
AU= 1
GM= 4*math.pi**2
dt= 0.001
t= 0
m= 1

class Planeta:
	def __init__(self, massa, x, y, vx, vy, x2, y2, x3, y3):
		self.m= massa
		self.x= x
		self.y= y
		self.r1= np.sqrt((x-x2)**2+(y-y2)**2)
		self.r2= np.sqrt((x-x3)**2+(y-y3)**2)
		self.vx= vx
		self.vy= vy
		
	def a(self, pos):
		at= -(GM/self.r1**3 + GM/self.r2**3)*pos
		return at
		
	def move(self):
		atx= self.a(self.x)
		self.x= self.x + self.vx*dt + 0.5*atx*dt**2
		self.vx= self.vx + atx*dt
		aty= self.a(self.y)
		self.y= self.y + self.vy*dt + 0.5*aty*dt**2
		self.vy= self.vy + aty*dt

p1=Planeta(1,1,0,0,0,0,np.sqrt(3),-1,0)
p2=Planeta(1,0,np.sqrt(5),0,0,1,0,-1,0)
p3=Planeta(1,-1,0,0,0,np.sqrt(3),0,1,0)

def wrap_angle(angle):
	return angle%360

pygame.init()
screen = pygame.display.set_mode((600,600)) #tamanho da imagem
myfont = pygame.font.Font(None,60) #fonte, tamanho

space = pygame.image.load("space.png").convert() # carrega imagem
planet = pygame.image.load("planeta.png").convert_alpha() 
sun = pygame.image.load("sun.png").convert_alpha() #alpha = transparencia
sun = pygame.transform.scale(sun,(100,100))

sunw,sunh = sun.get_size() #transforma em uma tupla
pygame.display.set_caption("3 planetas iguais")

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	planet = pygame.transform.scale(planet,(40,40))
	screen.blit(space, (0,0))
	#screen.blit(sun, (-50+300, -sunh/2+300))
	#xant,yant = terra.x, terra.y
	p1.move()
	p2.move()
	p3.move()
	#dx = terra.x - xant
	#dy = terra.y - yant
	#angulo = math.atan2(dy,dx)
	#angulo = wrap_angle(-math.degrees(angulo)+90)
	#dayplanet = pygame.transform.rotate(planet,angulo)
	screen.blit(planet, (p1.x*(600-20)/2 + (600-20)/2, p1.y*(600-20)/2 + (600-20)/2))
	screen.blit(planet, (p2.x*(600-20)/2 + (600-20)/2, p2.y*(600-20)/2 + (600-20)/2))
	screen.blit(planet, (p3.x*(600-20)/2 + (600-20)/2, p3.y*(600-20)/2 + (600-20)/2))
	pygame.display.update()
