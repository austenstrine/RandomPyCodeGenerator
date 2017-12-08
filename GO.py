from threading import Thread

class Go(Thread):
	"""This class is designed to quickly and easily run any function
	on a new thread."""
	
	def __init__(self, functionVar, optionalParameter0 = 'parameter not defined', optionalParameter1 = 'parameter not defined', optionalParameter2 = 'parameter not defined', optionalParameter3 = 'parameter not defined'):
		"""Defines any parameters necessary, attaches the function pointer as an attribute"""
		Thread.__init__(self)
		self.functionVar = functionVar
		if optionalParameter0 != 'parameter not defined':
			self.optionalParameter0 = optionalParameter0 
			if optionalParameter1 != 'parameter not defined':
				self.optionalParameter1 = optionalParameter1
				if optionalParameter2 != 'parameter not defined':
					self.optionalParameter2 = optionalParameter2
					if optionalParameter3 != 'parameter not defined':
						self.optionalParameter3 = optionalParameter3
		
	def run(self):
		"""Runs the function given, and includes any parameters"""
		fail = True
		try:
			self.functionVar(self.optionalParameter0, self.optionalParameter1, self.optionalParameter2, self.optionalParameter3)
			fail = False
		except AttributeError as ae:
#			print('fail', ae)
			pass
		if fail:
			try:
				self.functionVar(self.optionalParameter0, self.optionalParameter1, self.optionalParameter2)
				fail = False
			except AttributeError as ae:
#				print('fail', ae)
				pass
		if fail:
			try:
				self.functionVar(self.optionalParameter0, self.optionalParameter1)
				fail = False
			except AttributeError as ae:
#				print('fail', ae)
				pass
		if fail:
			try:
				self.functionVar(self.optionalParameter0)
				fail = False
			except AttributeError as ae:
#				print('fail', ae)
				pass
		if fail:
			self.functionVar()