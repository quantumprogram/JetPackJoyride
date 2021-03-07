
from entity import *

class vbar(entity):

	def __init__(self,x,y,game,size,marker,speed):
		entity.__init__(self,x,y,game)
		self.size=size
		self.marker=marker
		self.speed=speed

	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x-=self.speed
		if self.x < 0:
			self.permahide()
		self.render()

	def render(self):
		if(self.show):
			x=self.x
			y=self.y
			for i in range(self.size):
				self.game.canvas[y-i][x]=self.marker

	def check_collision(self):
		mand=self.game.charac
		bullets=self.game.m_bullet_list
		x=self.x
		y=self.y
		if(self.x >= mand.x and self.x < (mand.x + mand.size) and (not ((self.y-self.size > mand.y + mand.size) or (self.y < mand.y)))):
			return mand
		for bullet in bullets:
			if not bullet.is_alive:
				continue
			mand=bullet
			if(self.x >= mand.x and self.x < (mand.x + mand.size) and (not ((self.y-self.size > mand.y + mand.size) or (self.y < mand.y)))):
				return mand
		return None

class hbar(entity):

	def __init__(self,x,y,game,size,marker,speed):
		entity.__init__(self,x,y,game)
		self.size=size
		self.marker=marker
		self.speed=speed

	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x-=self.speed
		if self.x < 0:
			self.size=self.size+self.x
			self.x=0
		if self.size==0:
			self.permahide()
		self.render()

	def render(self):
		if(self.show):
			x=self.x
			y=self.y
			for i in range(self.size):
				self.game.canvas[y][x+i]=self.marker

	def check_collision(self):
		mand=self.game.charac
		bullets=self.game.m_bullet_list
		x=self.x
		y=self.y
		if(self.y >= mand.y and self.y < (mand.y + mand.size) and (not ((self.x + self.size < mand.x) or (mand.x + mand.size < self.x )))):
			return mand
		for bullet in bullets:
			if not bullet.is_alive:
				continue
			mand=bullet
			if(self.y >= mand.y and self.y < (mand.y + mand.size) and (not ((self.x + self.size < mand.x) or (mand.x + mand.size < self.x )))):
				return mand
		return None

class dbar(entity):

	def __init__(self,x,y,game,size,marker,speed):
		entity.__init__(self,x,y,game)
		self.size=size
		self.marker=marker
		self.speed=speed

	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x-=self.speed
		if self.x < 0:
			self.size=self.size+self.x
			self.x=0
			self.y-=1
		if self.size==0:
			self.permahide()
		self.render()

	def render(self):
		if(self.show):
			x=self.x
			y=self.y
			for i in range(self.size):
				self.game.canvas[y-i][x+i]=self.marker

	def does_collide2(self,x,y,size):
		points=[(x,y),(x+size-1,y+size-1),(x+size-1,y)]
		for x,y in points:
			for i in range(size):
				if x == self.x + i and y == self.y - i:
					print("Mando :"+str(x)+","+str(y))
					exit()
					return False
		return True

	def does_collide(self,x,y,size):		
		for i in range(0,size):
			if x+i in range(self.x,self.x + self.size):
				if y+i in range(self.y-self.size,self.y):
					return True		
		return False

	def check_collision(self):
		mand=self.game.charac
		bullets=self.game.m_bullet_list
		x=self.x
		y=self.y
		if(self.does_collide(mand.x,mand.y,mand.size)):
			return mand
		for bullet in bullets:
			if not bullet.is_alive:
				continue
			if self.does_collide(bullet.x,bullet.y,bullet.size):
				return bullet
		return None