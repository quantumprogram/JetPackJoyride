
from entity import entity 

class person(entity):

	def __init__(self,x,y,game,size,mark):
		super().__init__(x,y,game)
		self.size=size
		self.mark=mark
		
	
	def render(self):
		for i in range(self.size):
			for j in range(self.size):
				self.game.canvas[self.y+i][self.x+j]=self.mark

	def does_coillide(self,x,y,size):
		if x + size < self.x or self.x + self.size < x :
			return False
		if y + size < self.y or self.y + self.size < y :
			return False
		return True
		
	def check_collision(self):
		mand=self.game.charac
		bullets=self.game.m_bullet_list
		x=self.x
		y=self.y
		if self.does_coillide(mand.x,mand.y,mand.size):
			return mand
		for bullet in bullets:
			if not bullet.is_alive:
				continue
			if self.does_coillide(bullet.x,bullet.y,bullet.size):
				return bullet
		return None