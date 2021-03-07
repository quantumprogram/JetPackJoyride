from entity import entity
from person import person
class mando(person):

	def __init__(self,game):
		person.__init__(self,0,10,game,3,'M')

	def get_params(self, life, gravity, acceleration, speed, leftlimit, rightlimit, thrust):
		self.acceleration=acceleration
		self.speed=speed
		self.leftlimit=leftlimit
		self.rightlimit=rightlimit
		self.thrust=thrust
		self.gravity=gravity
		self.life=life

	def moveUp(self):
		thrust=self.thrust
		speed=self.speed
		self.gravity=0
		self.y-=thrust
		if(self.y<=(int(self.size/2))): 
			self.y=int(self.size/2)

	def moveDown(self):
		acceleration=self.acceleration
		self.y+=int(self.gravity)
		self.gravity=int(self.gravity+acceleration)
		if (self.y>=(len(self.game.canvas)-3-int(self.size/2))):
			self.y=len(self.game.canvas)-3-int(self.size/2)		
	def moveLeft(self):
		leftlimit=self.leftlimit
		self.gravity=0
		speed=self.speed
		self.x-=speed
		if(self.x<=leftlimit):
			self.x=leftlimit

	def moveRight(self):
		rightlimit=self.rightlimit
		self.gravity=0
		speed=self.speed
		self.x+=speed
		if(self.x>=rightlimit):
			self.x=rightlimit	

	def tick(self,input):
				
		
		if((self.is_alive)==False):
			return -1
		if input=="d":
			self.moveRight()
		
		if input=="a":
			self.moveLeft()				
        
		if input=="w":
			self.moveUp()

		self.moveDown()	

		

		if self.game.sbits > 0:
			self.mark='X' 	
		person.render(self)
		self.mark='M'



