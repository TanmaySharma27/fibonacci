'''fib class file'''
class fib(object):
	'''Creates class fib'''
	def __init__(self,n):
		self.n=n

	def print_ser(self):
		'''Creates print_series method'''
	#=input("enter the no. of terms - ")
		x=0
		y=1
		print x
		print y
		for x in range(self.n-2):
			z=x+y
			print z
			x=y
			y=z
	def print_hello(self):
		'''prints greetings'''
		print 'Hello, Wel-come to Python'
	def print_py(self):
		for i in range(self.n):
			for j in range(i):
				print (j+1),
			print

		for k in range(self.n,0,-1):
			for l in range(k):
				print l+1,
			print
	def print_all(self):
		self.print_ser()
		self.print_py()
		self.print_hello()
		

