
from entity import entity
from person import person
class shield(person):
	def __init__(self,x,y,game,size,marker,speed):
		self.speed=speed
		person.__init__(self,x,y,game,size,'S')
		self.size=size
		self.size=2
		self.y-=self.size
	
	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x-=self.speed
		if self.x < 0:
			self.permahide()
		person.render(self)
