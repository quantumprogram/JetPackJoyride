
import tty
import sys
import termios
import select

class input_grabber:

	def __init__(self):
		pass

	def isData(self):
		return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

	def grab(self):
		old_settings=termios.tcgetattr( sys.stdin )
		try:
			tty.setcbreak(sys.stdin.fileno())
			if self.isData():
				print("taking input")
				charvar=sys.stdin.read(1)
			else:
				print("no input to take")
				charvar=1
		finally:
			termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
		return charvar
