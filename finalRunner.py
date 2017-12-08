#Austen Loren Strine
import time, sys
import tkinter as k
import tkinter.scrolledtext as tkst
import pythonFinal
from io import StringIO
#from GO import Go
#from threading import Thread, RLock

root = k.Tk()
root.withdraw()

class BatchGUI(k.Frame):
	
	def __init__(self):
		""" """
		global root
		k.Frame.__init__(self)
		self.grid()
		self.master.title('Batch PyCode Generator - BaPyCoG')
		
		#widgets
		# batchSize = 0, given_input = 0, desired_output = 1, maxLines = 25, _minScope = 1, _maxScope = 5, _tabEntry = '\t', _newlineEntry = '\n'
		self._batchSizeLabel = k.Label(self, text = 'Batch Size:')
		self._batchSizeLabel.grid(row = 0, column = 0, sticky = 'nsew')
		self._batchSizeVar = k.StringVar(self, '1000')
		self._batchSizeEntry = k.Entry(self, textvariable = self._batchSizeVar)
#		self._batchSizeEntry.bind()
		self._batchSizeEntry.grid(columnspan = 5, row = 1, column = 0, sticky = 'nsew')
		
		self._givenInputLabel = k.Label(self, text = 'Input:')
		self._givenInputLabel.grid(row = 2, column = 0, sticky = 'nsew')
		self._givenInputVar = k.StringVar(self, '0')
		self._givenInputEntry = k.Entry(self, textvariable = self._givenInputVar)
#		self._givenInputEntry.bind()
		self._givenInputEntry.grid(columnspan = 5, row = 3, column = 0, sticky = 'nsew')
		
		self._desiredOutputLabel = k.Label(self, text = 'Desired Output:')
		self._desiredOutputLabel.grid(row = 4, column = 0, sticky = 'nsew')
		self._desiredOutputVar = k.StringVar(self, '1')
		self._desiredOutputEntry = k.Entry(self, textvariable = self._desiredOutputVar)
#		self._desiredOutputEntry.bind()
		self._desiredOutputEntry.grid(columnspan = 5, row = 5, column = 0, sticky = 'nsew')
		
		self._maxLinesLabel = k.Label(self, text = 'Max Length in Level 0 Scope Phrases:')
		self._maxLinesLabel.grid(row = 6, column = 0, sticky = 'nsew')
		self._maxLinesVar = k.StringVar(self, '3')
		self._maxLinesEntry = k.Entry(self, textvariable = self._maxLinesVar)
#		self._maxLinesEntry.bind()
		self._maxLinesEntry.grid(columnspan = 5, row = 7, column = 0, sticky = 'nsew')

		self._minScopeVar = k.StringVar(self, '1')
		
		self._maxScopeLabel = k.Label(self, text = 'Max Scope Depth:')
		self._maxScopeLabel.grid(row = 8, column = 0, sticky = 'nsew')
		self._maxScopeVar = k.StringVar(self, '3')
		self._maxScopeEntry = k.Entry(self, textvariable = self._maxScopeVar)
#		self._maxScopeEntry.bind()
		self._maxScopeEntry.grid(columnspan = 5, row = 9, column = 0, sticky = 'nsew')
		
#		self._tabLabel = k.Label(self, text = 'Tab Symbol:')
#		self._tabLabel.grid(row = 10, column = 0, sticky = 'nsew')
		self._tabVar = k.StringVar(self, '\t')
#		self._tabEntry = k.Entry(self, textvariable = self._tabVar)
#		self._tabEntry.bind()
#		self._tabEntry.grid(columnspan = 5, row = 11, column = 0, sticky = 'nsew')
		
#		self._newlineLabel = k.Label(self, text = 'Newline Symbol:')
#		self._newlineLabel.grid(row = 12, column = 0, sticky = 'nsew')
		self._newlineVar = k.StringVar(self, '\n')
#		self._newlineEntry = k.Entry(self, textvariable = self._newlineVar)
#		self._newlineEntry.bind()
#		self._newlineEntry.grid(columnspan = 5, row = 13, column = 0, sticky = 'nsew')
		
		self._goButton = k.Button(self, command = self.runBatch, text = 'Generate Code')
		self._goButton.grid(row = 14, column = 5, sticky = 'nsew')
		
		self._generatedCode = tkst.ScrolledText(self, wrap = 'word')
		self._generatedCode.bind("<1>", lambda event: self._generatedCode.focus_set())
		self._generatedCode.config(state='disabled')
		self._generatedCode.grid(rowspan = 8, columnspan = 4, row = 14, column = 0)
		
#		self._generatedCode.config(state='normal')
#		self._generatedCode.delete('1.0', 'end')
#		self._generatedCode.insert('1.0', 'the text you want to insert')
#		self._generatedCode.see('end')
#		self._generatedCode.config(state='disabled')
		
		for row in range(22):
			root.rowconfigure(row, weight = 1)
		for column in range(5):
			root.columnconfigure(column, weight = 1)	
				
		root.protocol('WM_DELETE_WINDOW', self._closeWindow)
		root.deiconify()
		
		#misc properties
		self.continueThread = True
		self.code_gen = pythonFinal.CodeFileGenerator()
		
	def runBatch(self):
		""" """
		old_stdout = sys.stdout
		redirected_output = StringIO()
		sys.stdout = redirected_output
		self.code_gen.beginBatchRun(int(self._batchSizeVar.get()), int(self._givenInputVar.get()), int(self._desiredOutputVar.get()), int(self._maxLinesVar.get()), int(self._minScopeVar.get()), int(self._maxScopeVar.get()), self._tabVar.get(), self._newlineVar.get()) #redirected_output catches the 'return' value here
		sys.stdout = old_stdout	
		batchString = redirected_output.getvalue()
		
		self._generatedCode.config(state='normal')
		self._generatedCode.delete('1.0', 'end')
		self._generatedCode.insert('1.0', batchString)
		self._generatedCode.see('end')
		self._generatedCode.config(state='disabled')
				
		return 'batch run ended'
		
	def _closeWindow(self):
		global root
		self.continueThread = False
		self.destroy()
		root.destroy()


def main():
	""" """
	window = BatchGUI()
	window.mainloop()

main()

#Austen Loren Strine