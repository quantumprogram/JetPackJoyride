
class entity:                                             
														   	
	def __init__(self,x,y,game):
		self.x=x
		self.y=y
		self.game=game
		self.show=True
		self.game.add_entity(self)
		self.is_alive=True

	def hide(self):
		self.show=False

	def display(self):
		if self.is_alive:
			self.show=True

	def permahide(self):
		self.is_alive=False
		self.show=False

	def tick(self):
		pass

	def render(self):
		pass