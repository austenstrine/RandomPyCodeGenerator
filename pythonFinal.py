#Austen Loren Strine
import sys
from io import StringIO
from random import randint

#############GENERATED CODE PRINTS RESULT, DOES NOT RETURN RESULT#############

class Stack(object):
	def __init__(self):
		self.items = []
		
	def __len__(self):
		return self.size()

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

class CodeFileGenerator(object):
	def __init__(self, batchSize = 0, given_input = 0, desired_output = 1, max_lines = 25, min_scope = 1, max_scope = 5, tab = '\t', newline = '\n'):
		self.GIVEN_INPUT = given_input
		self.DESIRED_OUTPUT = desired_output
		self.MAX_LINES = max_lines
		self.LETTER_LIST = ['A', 'b', 'c', 'd', 'E', 'f', 'g', 'h', 'I', 'j', 'k', 'l', 'm', 'n', 'O', 'p', 'q', 'r', 's', 't', 'U', 'v', 'w', 'x', 'Y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
		self.COMPARATIVE_OPERATOR_LIST = [' ==',' !=',' <',' >',' <=',' >=',' is']
		self.MUTATORS = [' +',' -']#,' *',' /']
		self.MUT_ASSIGN = [' +=', ' -=']
		self.ASSIGNMENT = ' ='
		self.TAB = tab
		self.NEWLINE = newline
		self.RETURN = 'print('
		self.RETURN_END = ')'
		self.END = 'return'
		self.CONDITIONAL_LIST = ['if']
		self.MAX_SCOPE = max_scope
		self.MIN_SCOPE = min_scope
		self.STARTING_STRING = 'def main():' + self.NEWLINE \
		+ self.TAB + 'givnInput = ' + str(self.GIVEN_INPUT) + self.NEWLINE
		self.ALTERNATE_STARTING_STRING = 'def main():' + self.NEWLINE \
		+ self.TAB + 'givnInput = ' + str(self.GIVEN_INPUT+10) + self.NEWLINE
		self.ENDING_STRING = self.NEWLINE + 'main()'+ self.NEWLINE 
		self.current_lines = 0
		self.end = False
		self.completeFile = ''
		self.variable_names = Stack() 
		self.variable_names.push(['givnInput'])
		self.scope_depth = int(self.MIN_SCOPE)
		self.firstLine = True
		self.batchSize = batchSize
		self.returnDeclared = False
		self.OPTIONS = [self.genConditional, self.genNewVariable, self.genAlterVariable, self.genReturn, self.decrementScope]
		self.fileString = ''
		self.newVariableMade = True
		self.debugNames = []
		self.batchNumber = 0

	def makeDebugFile(self, filename, content):
		if filename in self.debugNames:
			with open(filename+str(self.batchNumber)+'.txt', 'w+') as f:
				f.write(content)
			self.debugNames.append(filename)
		else:
			with open(filename+str(self.batchNumber)+'.txt', 'a+') as f:
				f.write(content)

	def randVarInScope(self):
		""" """
		upperBound = len(self.variable_names.peek())-1
		randomVarIndex = None
		rint = randint(1,3)
		if rint == 1:
			randomVarIndex = randint(0, upperBound)
		elif rint == 2:
			randomVarIndex = randint(int(upperBound/2), upperBound)
		else:
			randomVarIndex = randint(int(upperBound/4)*3, upperBound)
		return self.variable_names.peek()[randomVarIndex]

	def mkTab(self):
		""" """
		#self.makeDebugFile('debugTS', 'TabScope: '+str(self.scope_depth)+self.NEWLINE)
		return self.TAB*self.scope_depth
		
	def getValOrVar(self):
		""" """
		return self.genConditionalVals()[randint(0, 1)]

	def genConditionalVals(self):
		""" """
		result1 = self.variable_names.peek()[randint(0, len(self.variable_names.peek())-1)]
		igr = randint(1, 2)
		result2 = None
		if igr == 1:
			result2 = str(randint(self.DESIRED_OUTPUT-self.DESIRED_OUTPUT*2-1, self.DESIRED_OUTPUT*2+1))
		else:
			result2 = self.randVarInScope()
		return (result1, result2)
		
	def genMutPhrase(self):
		""" """
		phrase = self.randVarInScope()+ ' ' + self.MUTATORS[randint(0, 1)] + ' ' + self.getValOrVar()
		return phrase 
		
#	def endCodeGeneration(self):
#		""" """
#		self.end = True
		
	def decrementScope(self):
		"""To be used at the end of loops, conditionals, and any other such structures to ensure proper tablature"""
		if self.returnDeclared:
			if self.scope_depth-1 < self.MIN_SCOPE:
				self.scope_depth -= 1
				self.end = True
				return ''
		if self.scope_depth <= self.MIN_SCOPE:
			if self.returnDeclared:
#				self.endCodeGeneration()
				self.end = True
				return ''
			else:
				return self.OPTIONS[3]()
		self.variable_names.pop()#deletes top level
		#self.makeDebugFile('debugTS', 'PreDecrement Scope: '+str(self.scope_depth)+self.TAB)
		self.scope_depth -= 1
		#self.makeDebugFile('debugTS', 'PostDecrement Scope: '+str(self.scope_depth)+self.NEWLINE)
		self.returnDeclared = False
		return ''
		
	def genReturn(self):
		"""Generates a string representation of a return statement"""
		#need code to track actions taken in scope, and ensure that other actions are taken before a return statement is generated
		statement = None
		self.returnDeclared = True
		r = randint(1, 3)
		if r == 1:
			var = self.randVarInScope()
			statement = self.mkTab() + self.RETURN + var + self.RETURN_END + self.NEWLINE + self.mkTab() + self.END + ' ' + var + self.NEWLINE
			#code to determine which variable will be chosen to return
		else:
			var = self.genMutPhrase()
			statement = self.mkTab() + self.RETURN + var + self.RETURN_END + self.NEWLINE + self.mkTab() + self.END + ' ' + var + self.NEWLINE
		statement += self.decrementScope()# + '#Decremented RETURN\n'
#		statement = self.mkTab()+'#return generated' + self.NEWLINE + statement
		return statement
		
	def genNewVariable(self):
		"""Generates a string representation of a new varialbe, and data to assign it to"""
		length = randint(1, 5)
		string = ''
		LLLength = len(self.LETTER_LIST)
		while length > 0:
			string += self.LETTER_LIST[randint(0, LLLength-1)]
			length -= 1
#		print(self.scope_depth)
		tabbedString = self.mkTab()+string
		tabbedString += self.ASSIGNMENT + ' ' + self.getValOrVar() + self.NEWLINE #code to determine whether this assignment should combine/mutate existing vars
		if not string in self.variable_names.peek():
			lister = list(self.variable_names.pop())
			lister.append(string)
			self.variable_names.push(lister)
		else:
#			return self.mkTab()+'#New variable exists, generating again' + self.NEWLINE + self.genNewVariable()
			return self.genNewVariable()
#		tabbedString = self.mkTab()+'#New variable generated' + self.NEWLINE+ tabbedString
		return tabbedString
		
	def genAlterVariable(self):
		"""Generates a string representation of an alteration of an existing variable"""
		existing = self.mkTab() + self.randVarInScope() #track choice here
		if randint(0, 1) == 1:
			existing += self.MUT_ASSIGN[randint(0, 1)] + ' ' + self.getValOrVar() #track choice here
		else:
			existing += self.ASSIGNMENT + ' ' +  self.getValOrVar() + self.MUTATORS[randint(0, 1)] + self.getValOrVar() #track choice here
		existing += self.NEWLINE
#		existing = self.mkTab()+'#Existing variable altered, scope is '+str(self.scope_depth) + self.NEWLINE + existing
		return existing
		
	
	def genConditional(self):
		"""Generates a string representation of a conditional statement"""
		if self.end:
			return self.decrementScope()
		self.variable_names.push(self.variable_names.peek())
		conditionalResult = 0#some code to determine the type of conditional
		operatorResult = randint(0, 6)
		optionsResult = None
		value1Result, value2Result = self.genConditionalVals()
		string = self.mkTab() + self.CONDITIONAL_LIST[conditionalResult] + ' ' + value1Result + ' ' + self.COMPARATIVE_OPERATOR_LIST[operatorResult] + ' ' + value2Result + ':' + self.NEWLINE
		self.scope_depth += 1
		if self.scope_depth < self.MAX_SCOPE:
			optionsResult = randint(0, 3)#keep track of which items/values were chosen so the algorithm can learn, have it be random at first, then deterministic once enough data has been gathered. Will need a 'gathered data threshold' so that if above threshold, different code is executed based on results of data. Maybe something like 10,000 algorithms
#			string += self.mkTab()+'#Conditional, self.scope_depth < self.MAX_SCOPE and not self.end' + self.NEWLINE
			string += self.OPTIONS[optionsResult]()
		else:
			self.end = True
#			while not self.returnDeclared:
			if self.returnDeclared:
				string += self.decrementScope()# + '#Decremented IF\n'
			else:
				string += self.genReturn()# + '#Returned IF\n'
			return string
		if optionsResult != 3:
			string += self.decrementScope()# + '#Decremented IF\n'
#		string = self.mkTab()+'#Conditional generated' + self.NEWLINE + string
		return string

	def resetVariables(self):
		""" """
		self.current_lines = 0
		self.end = False
		self.completeFile = ''
		self.variable_names = Stack() 
		self.variable_names.push(['givnInput'])
		self.scope_depth = int(self.MIN_SCOPE)
		self.returnDeclared = False
		self.batchSize += 1
		self.fileString = ''

	
	def beginBatchRun(self, batchSize = 0, given_input = 0, desired_output = 1, max_lines = 25, min_scope = 1, max_scope = 5, tab = '\t', newline = '\n', makeResultsFile = False):
		if batchSize > 50000:
			print('Batch size too large!')
			return 'Batch size too large!'
		self.batchSize = batchSize
		self.GIVEN_INPUT = given_input
		self.DESIRED_OUTPUT = desired_output
		self.MAX_LINES = max_lines
		self.MIN_SCOPE = min_scope
		self.MAX_SCOPE = max_scope
		self.TAB = tab
		self.NEWLINE = newline
		self.STARTING_STRING = 'def main():' + self.NEWLINE \
		+ self.TAB + 'givnInput = ' + str(self.GIVEN_INPUT) + self.NEWLINE
		self.ALTERNATE_STARTING_STRING = 'def main():' + self.NEWLINE \
		+ self.TAB + 'givnInput = ' + str(self.GIVEN_INPUT+10) + self.NEWLINE
		
		batchResults = ''
		batchSuccessOnly = ''
		for index in range(self.batchSize-1):
			self.batchNumber = index
			#generates the file string:	
			self.resetVariables()
			pong = True
			while True:#this doesn't actually translate to 'lines', I know
				if self.current_lines >= self.MAX_LINES or self.end:
					if self.end:
						if self.returnDeclared:
							break
						else:
							while not self.returnDeclared:
								self.fileString += self.OPTIONS[3]()
					self.fileString += self.OPTIONS[4]()
				else:
					if self.newVariableMade:
						self.fileString += self.OPTIONS[randint(0, 2)]()
						self.current_lines += 1
						self.newVariableMade = False
					else:
						if pong: #generates 50% less returns AND decrements
							self.fileString += self.OPTIONS[randint(0, 2)]()
							self.current_lines += 1
							pong = False
						else:
							self.fileString += self.OPTIONS[randint(0, 4)]()
							self.current_lines += 1
							pong = True
					
			#File string generated.
			output = None
			
			try:
				old_stdout = sys.stdout
				redirected_output = StringIO()
				sys.stdout = redirected_output
	##			with open('debug.txt', 'w+') as db:
	##				db.write(self.STARTING_STRING + self.fileString + self.ENDING_STRING)
				exec(self.STARTING_STRING + self.fileString + self.ENDING_STRING)
				sys.stdout = old_stdout	
				output = int(redirected_output.getvalue().strip())
			except Exception as ve:
				self.makeDebugFile('debug', str(ve)+'\n'+self.STARTING_STRING + self.fileString + self.ENDING_STRING)
				print('Error! Check debug.txt')
				return 'Error! Check debug.txt'
			if output == self.DESIRED_OUTPUT:
				try:
					old_stdout = sys.stdout
					redirected_output = StringIO()
					sys.stdout = redirected_output
					exec(self.ALTERNATE_STARTING_STRING + self.fileString + self.ENDING_STRING)
					sys.stdout = old_stdout	
					alternateOutput = int(redirected_output.getvalue().strip())
					
					if output == alternateOutput:
						result = str(alternateOutput) + ' False, always == desired output\t' + str(index) + self.NEWLINE#  \
                                                         #+ str(self.STARTING_STRING + self.fileString + self.ENDING_STRING)
						batchResults += '\n'+result
					else:
						result = str('\nSUCCESS!' \
                                                             + self.NEWLINE + self.STARTING_STRING + self.fileString + self.ENDING_STRING)
						batchSuccessOnly += '\n'+result
						batchResults += '\n\n'+result
				except Exception as e:
					self.makeDebugFile('debug', str(e)+'\n'+self.ALTERNATE_STARTING_STRING + self.fileString + self.ENDING_STRING)
					batchResults += str(e)+'\n'
			else:
				result = str(output) + ' False, != desired output\t' + str(index) + self.NEWLINE #\
                                         #+ str(self.STARTING_STRING + self.fileString + self.ENDING_STRING)
				batchResults += '\n'+result
		if makeResultsFile:
			for i in range(0, 9999):
				try:
					with open('batchResults'+str(i)+'.txt', 'r'):
						pass
				except IOError:
					
					with open('batchResults'+str(i)+'.txt', 'w+') as br:
						br.write(batchResults)
					batchResults = 'Detailed results in \'batchResults'+str(i)+'.txt\'\n'+str(batchSuccessOnly)
					break
		else:
			print(str(batchSuccessOnly))
			return str(batchSuccessOnly)

#def main(batchSize = 0, given_input = 0, desired_output = 1, max_lines = 25, min_scope = 1, max_scope = 5, tab = '\t', newline = '\n'):
#	return CodeFileGenerator(batchSize = 0, given_input = 0, desired_output = 1, max_lines = 25, min_scope = 1, max_scope = 5, tab = '\t', newline = '\n').beginBatchRun()
#main()
#Austen Loren Strine



			
			
