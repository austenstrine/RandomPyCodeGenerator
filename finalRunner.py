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
		self._batchSizeLabel.grid(row = 0, column = 1, sticky = 'nsw', pady = (20,0),padx = (25, 25))
		self._batchSizeVar = k.StringVar(self, '1000')
		self._batchSizeEntry = k.Entry(self, textvariable = self._batchSizeVar)
#		self._batchSizeEntry.bind()
		self._batchSizeEntry.grid(columnspan = 2, row = 1, column = 1, sticky = 'nsew', padx = (25, 25))
		
		self._givenInputLabel = k.Label(self, text = 'Input:')
		self._givenInputLabel.grid(row = 2, column = 1, sticky = 'nsw', padx = (25, 25))
		self._givenInputVar = k.StringVar(self, '0')
		self._givenInputEntry = k.Entry(self, textvariable = self._givenInputVar)
#		self._givenInputEntry.bind()
		self._givenInputEntry.grid(columnspan = 2, row = 3, column = 1, sticky = 'nsew', padx = (25, 25))
		
		self._desiredOutputLabel = k.Label(self, text = 'Desired Output:')
		self._desiredOutputLabel.grid(row = 4, column = 1, sticky = 'nsw', padx = (25, 25))
		self._desiredOutputVar = k.StringVar(self, '1')
		self._desiredOutputEntry = k.Entry(self, textvariable = self._desiredOutputVar)
#		self._desiredOutputEntry.bind()
		self._desiredOutputEntry.grid(columnspan = 2, row = 5, column = 1, sticky = 'nsew', padx = (25, 25))
		
		self._maxLinesLabel = k.Label(self, text = 'Max Length in "Scope Level 0" Phrases:\n(Lower value means fewer lines of code)')
		self._maxLinesLabel.grid(row = 6, column = 1, sticky = 'nsw', padx = (25, 25))
		self._maxLinesVar = k.StringVar(self, '3')
		self._maxLinesEntry = k.Entry(self, textvariable = self._maxLinesVar)
#		self._maxLinesEntry.bind()
		self._maxLinesEntry.grid(columnspan = 2, row = 7, column = 1, sticky = 'nsew', padx = (25, 25))

		self._minScopeVar = k.StringVar(self, '1')
		
		self._maxScopeLabel = k.Label(self, text = 'Max Scope Depth:')
		self._maxScopeLabel.grid(row = 8, column = 1, sticky = 'nsw', padx = (25, 25))
		self._maxScopeVar = k.StringVar(self, '3')
		self._maxScopeEntry = k.Entry(self, textvariable = self._maxScopeVar)
#		self._maxScopeEntry.bind()
		self._maxScopeEntry.grid(columnspan = 2, row = 9, column = 1, sticky = 'nsew', padx = (25, 25))
		
#		self._tabLabel = k.Label(self, text = 'Tab Symbol:')
#		self._tabLabel.grid(row = 10, column = 0, sticky = 'nsew')
		self._tabVar = k.StringVar(self, '\t')#Eventually, this will be an adjustable setting
#		self._tabEntry = k.Entry(self, textvariable = self._tabVar)
#		self._tabEntry.bind()
#		self._tabEntry.grid(columnspan = 5, row = 11, column = 0, sticky = 'nsew')
		
#		self._newlineLabel = k.Label(self, text = 'Newline Symbol:')
#		self._newlineLabel.grid(row = 12, column = 0, sticky = 'nsew')
		self._newlineVar = k.StringVar(self, '\n')#Eventually, this will be an adjustable setting
#		self._newlineEntry = k.Entry(self, textvariable = self._newlineVar)
#		self._newlineEntry.bind()
#		self._newlineEntry.grid(columnspan = 5, row = 13, column = 0, sticky = 'nsew')
		
		self._goButton = k.Button(self, command = self.runBatch, text = 'Generate Code')
		self._goButton.grid(row = 37, column = 1, sticky = 'nsew', padx = (25, 25))
		self._generatedCode = tkst.ScrolledText(self, wrap = 'word')
		self._generatedCode.bind("<1>", lambda event: self._generatedCode.focus_set())
		self._generatedCode.config(state='disabled', highlightthickness = 1)
		self._generatedCode.grid(rowspan = 48, row = 0, column = 0, pady = (25, 25), padx = (25, 0))
		
		self._cbxVar = k.IntVar(0)
		self._makeResultsFileCbx = k.Checkbutton(self, text = "Generate Results File", variable = self._cbxVar)
		self._makeResultsFileCbx.grid(row = 10, column = 1)
		
		for row in range(23):
			root.rowconfigure(row, weight = 1)
		for column in range(4):
			root.columnconfigure(column, weight = 1)	
				
		root.protocol('WM_DELETE_WINDOW', self._closeWindow)
		root.deiconify()
		self._generatedCode.focus_force()
		
		#misc properties
		self.continueThread = True
		self.code_gen = pythonFinal.CodeFileGenerator()
		
	def runBatch(self):
		""" """
		old_stdout = sys.stdout
		redirected_output = StringIO()
		sys.stdout = redirected_output
		self.code_gen.beginBatchRun(int(self._batchSizeVar.get()), int(self._givenInputVar.get()), int(self._desiredOutputVar.get()), int(self._maxLinesVar.get()), int(self._minScopeVar.get()), int(self._maxScopeVar.get()), self._tabVar.get(), self._newlineVar.get(), self._cbxVar.get()) #redirected_output catches the 'return' value here
		sys.stdout = old_stdout	
		batchString = redirected_output.getvalue()
		
		self._generatedCode.config(state='normal')
		self._generatedCode.delete('1.0', 'end')
		self._generatedCode.insert('1.0', batchString)
		self._generatedCode.see('1.0')
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