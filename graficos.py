#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math

G= 6.67*10**-11
AU= 1
GM= 4*math.pi**2
dt= 0.0001
t=0
m= 1

class Planeta:
	def __init__(self, massa, x, y, vx, vy):
		self.m= massa
		self.x= x
		self.y= y
		self.r= np.sqrt(x**2+y**2)
		self.vx= vx
		self.vy= vy
		self.v= np.sqrt(vx**2+vy**2)
		self.e= 0.5*massa*(vx**2+vy**2) - GM*m/self.r
		
	def a(self, pos):
		r= np.sqrt(self.x**2+self.y**2)
		at= -(GM/r**3)*pos
		return at
		
	def move(self, t):
		atx= self.a(self.x)
		self.x= self.x + self.vx*dt + 0.5*atx*dt**2
		self.vx= self.vx + atx*dt
		aty= self.a(self.y)
		self.y= self.y + self.vy*dt + 0.5*aty*dt**2
		self.vy= self.vy + aty*dt
		self.e= 0.5*m*(self.vx**2+self.vy**2) - GM*m/self.r
		self.r= np.sqrt(self.x**2+self.y**2)
		self.v= np.sqrt(self.vx**2+self.vy**2)
		
p1=Planeta(1,1,0,0,2*np.pi)#
	
	
tmax=4
t=np.arange(0, tmax, dt)
x=np.zeros(t.size)
y=np.zeros(t.size)
r=np.zeros(t.size)
vx=np.zeros(t.size)
vy=np.zeros(t.size)
v=np.zeros(t.size)

for i in range (t.size):
	p1.move(t[i])
	x[i]=p1.x
	y[i]=p1.y
	r[i]=p1.r
	vx[i]=p1.vx
	vy[i]=p1.vy
	v[i]=p1.v
	
plt.figure(figsize=(8,5),dpi=100)
plt.axes().set_aspect('equal','datalim')
ax=plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.autoscale()

plt.rc('text',usetex=True)
plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
plt.title(r'\textnormal{Espaco de fases (x por vx)}',fontsize=12)#

plt.plot (x,vx, 'r-', linewidth=1)#
plt.legend(loc="upper right")
plt.grid()
plt.savefig("espacodefases1.pdf",dpi=96)#
plt.show()	
