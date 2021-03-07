from person import person
class d_bullet(person):
	def __init__(self,x,y,game,size,mark,speed):
		x=game.boss.x+game.boss.size-1
		y=game.boss.y+1
		size=1
		person.__init__(self,x,y,game,size,mark)
		self.speed=speed
		self.game.add_d_bullet(self)
		
        
	def tick(self):
		if self.is_alive == False:
			return -1 
		self.x-=self.speed
		if self.x <= 0:
		    self.permahide()
		person.render(self)
