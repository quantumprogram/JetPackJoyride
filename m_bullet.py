
from person import person
class m_bullet(person):
	def __init__(self,x,y,game,size,mark,speed):
		x=game.charac.x+game.charac.size+1
		y=game.charac.y+1
		size=1
		mark='>'
		person.__init__(self,x,y,game,size,mark)
		self.speed=speed
		self.game.add_m_bullet(self)
		
        
	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x+=self.speed
		if self.x >= (self.game.xlen-10):
		    self.permahide()
		person.render(self)
