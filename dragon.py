
from person import person
class dragon(person):
	def __init__(self,x,y,game,size,mark,leftmost,speed,lives):
		x=game.xlen-10
		y=game.charac.y
		size=game.charac.size
		mark='D'
		person.__init__(self,x,y,game,size,mark)
		self.leftmost=leftmost
		self.speed=speed
		self.lives=lives

	def moveleft(self):
		self.x=self.x-self.speed	
		if(self.x<self.leftmost):
			self.x=self.leftmost	

	def moveUp(self):
		self.y=self.y-self.speed
	def moveDown(self):
		self.y=self.y+self.speed	

	def tick(self):
		if((self.is_alive)==False):
			return -1
		k=self.y-(self.game.charac.y)
		if k>=0:
			self.moveUp()
		else:
			self.moveDown()	
		self.moveleft()
		person.render(self)

