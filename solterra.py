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
	def __init__(self, massa, x, y, vx, vy):
		self.m= massa
		self.x= x
		self.y= y
		self.r= np.sqrt(x**2+y**2)
		self.vx= vx
		self.vy= vy
		self.e= 0.5*massa*(vx**2+vy**2) - GM*m/self.r
		
	def a(self, pos):
		r= np.sqrt(self.x**2+self.y**2)
		at= -(GM/r**3)*pos
		return at
		
	def move(self):
		atx= self.a(self.x)
		self.x= self.x + self.vx*dt + 0.5*atx*dt**2
		self.vx= self.vx + atx*dt
		aty= self.a(self.y)
		self.y= self.y + self.vy*dt + 0.5*aty*dt**2
		self.vy= self.vy + aty*dt
		self.e= 0.5*m*(self.vx**2+self.vy**2) - GM*m/self.r

terra=Planeta(1,1,0,0,2*np.pi)

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
pygame.display.set_caption("O Sol e a Terra")

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	planet = pygame.transform.scale(planet,(40,40))
	screen.blit(space, (0,0))
	screen.blit(sun, (-50+300, -sunh/2+300))
	xant,yant = terra.x, terra.y
	terra.move()
	dx = terra.x - xant
	dy = terra.y - yant
	angulo = math.atan2(dy,dx)
	angulo = wrap_angle(-math.degrees(angulo)+90)
	dayplanet = pygame.transform.rotate(planet,angulo)
	screen.blit(dayplanet, (terra.x*(600-20)/2 + (600-20)/2, terra.y*(600-20)/2 + (600-20)/2))
	pygame.display.update()
