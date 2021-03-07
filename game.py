
import os
import sys
import random
#from input_grabber import input_grabber
from input_grabber2 import Input
from mando import mando
import time
from obstacles import vbar, hbar, dbar
from coin import coins
from shield import shield
from magnet import magnet
from m_bullet import m_bullet
from d_bullet import d_bullet
from dragon import dragon

class game:

	entity_list=[]
	m_bullet_list=[]
	d_bullet_list=[]
	spawnables=[0,vbar,hbar,dbar,coins,shield,magnet]
	score=0
	tokens=0
	sbits=0
	lives=5
	speedup_available=True
	speedup_at=-1
	tick_rate=1/24
	victory=False
	dragon_tick=300
	boss = None

	def __init__(self,xlen,ylen):
		self.xlen=xlen
		self.ylen=ylen
		self.canvas=[ [ " " for x in range(xlen)] for y in range(ylen+2) ]
		self.refresh_canvas()
		self.make_mando()
		self.entity_list=[]

	def refresh_canvas(self):
		xlen=self.xlen
		ylen=self.ylen
		for i in range(xlen):
			self.canvas[0][i]='-'
			for j in range(1,ylen+1):
				self.canvas[j][i]=" "
			self.canvas[ylen+1][i]='-'

	def draw_canvas(self):
		os.system('clear')
		outstring=""
		canvas=self.canvas
		for i in range(self.ylen+2):
			outstring+="\n"
			for j in range(self.xlen):
				outstring+=canvas[i][j]
		outstring+="\n"
		#print(outstring)
		os.write(1,str.encode(outstring))

	def add_entity(self,entity):
		self.entity_list.append(entity)

	def add_m_bullet(self,bullet):
		self.m_bullet_list.append(bullet)

	def add_d_bullet(self,bullet):	
		self.d_bullet_list.append(bullet)

	def make_mando(self):
		self.charac=mando(self)
		self.charac.get_params(2, 1, 1, 1, 1, self.xlen -20, 2)

	def make_dragon(self):	
		self.boss=dragon(0,0,self,3,'D',self.xlen-30,1,3)

	def run(self):
		ticks=0
		INPUT=Input()
		while True:
			time.sleep(self.tick_rate)
			self.refresh_canvas()
			if ticks % 10 == 0 and ticks < self.dragon_tick:
				x=random.choice(self.spawnables)
				if x!=0:
					x=x(self.xlen-20, random.randint(11,self.ylen-1),self,10,'O',3)
					x.display()
			if ticks > self.dragon_tick:
				if self.boss == None:
					self.make_dragon()
				if ticks%5==0:	
					D_bullet=d_bullet(0,0,self,1,'<',2)	
					D_bullet.display()
			inp='o'
			if INPUT.check_stream():
				inp = INPUT.get_from_stream()
			INPUT.clear_stream()
			if inp=='q' :
				break
			if inp=='v' :
				if self.speedup_available:
					self.speedup_available=False
					self.tick_rate=self.tick_rate/5
					self.speedup_at=ticks
			if inp=='f':
				M_bullet=m_bullet(0,0,self,1,'>',2)
				M_bullet.display()
			self.charac.tick(inp)
			for entity in self.entity_list:
				entity.tick()
			for entity in self.entity_list:
				if not entity.is_alive:
					continue
				if type(entity) is coins:
					if entity.check_collision()	== self.charac:
						self.tokens+=1
						entity.permahide()
				if type(entity) is shield:
					if entity.check_collision() == self.charac:
						self.sbits+=1
						entity.permahide()
				if type(entity) is vbar or type(entity) is hbar or type(entity) is dbar:
					if entity.check_collision() == self.charac:
						if self.sbits > 0:
							self.sbits-=1
						else:
							self.lives-=1
						if self.lives == 0:
							print("Game over!")
							exit()
						else:
							entity.permahide()
					if type(entity.check_collision()) is m_bullet:
						entity.check_collision().permahide()
						entity.permahide()
				if type(entity) is dragon:
					if type(entity.check_collision()) == m_bullet:
						self.boss.lives-=1
						if self.boss.lives == 0:
							print("victory")
							exit()
				if type(entity) is d_bullet:
					if entity.check_collision() == self.charac:
						if self.sbits > 0:
							self.sbits-=1
						else:
							self.lives-=1
						if self.lives == 0:
							print("Game over! But nice try")
							exit()

			self.score=ticks/200 + self.tokens
			self.draw_canvas()
			print("Lives = " + str(self.lives) + " Shield = " + str(self.sbits))
			print("Coins = " + str(self.tokens))
			print("Score = " + str(self.score))
			#for entity in self.entity_list:
				#print(type(entity))
			if self.speedup_at > 0 and ticks > self.speedup_at + 250:
				self.tick_rate=self.tick_rate*5
				self.speedup_at=-1
			ticks+=1
