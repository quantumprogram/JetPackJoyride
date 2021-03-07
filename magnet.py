from entity import entity
from person import person
class magnet(person):
	def __init__(self,x,y,game,size,marker,speed):
		self.speed=speed
		person.__init__(self,x,y,game,size,'U')
		self.size=size
		self.size=2
		self.y-=self.size
	
	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x-=self.speed
		if self.x < 0:
			self.permahide()
		if self.x > self.game.charac.x:
			self.game.charac.moveRight()
		else:
			self.game.charac.moveLeft()
		if self.y > self.game.charac.y:
			self.game.charac.moveDown()
		else:
			self.game.charac.moveUp()
		person.render(self)