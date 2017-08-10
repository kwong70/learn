
from threading import Thread

class myThread(Thread):
	def __init__( self, ID): #constructor
		Thread.__init__(self)
		self.ID = ID 

	def run(self): #the method you want to execute multiple times 
		print self.ID 


for i in range(5):
	t = myThread(i)
	t.start()