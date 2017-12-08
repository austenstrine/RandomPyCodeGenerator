import sys
from io import StringIO

def main():
	GIVEN_INPUT = input('Enter input as an integer:')
	code = "def main():\n\tinput = "+GIVEN_INPUT+"\n\tprint(input + 3)\nmain()"
	
	old_stdout = sys.stdout
	redirected_output = StringIO()
	sys.stdout = redirected_output

	exec(code)#, sys._getframe(1).f_globals, sys._getframe(1).f_locals)
		
	sys.stdout = old_stdout	
	
	print('function completed')
	OUTPUT = redirected_output.getvalue().strip()
	print(OUTPUT+' is the result of:\n'+ code)
	
main()
