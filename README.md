# RandomPyCodeGenerator
A program that randomly generates Python code, and then filters based on the desired outcome

## Basic Function
  This is a code generation program. You can input a given integer, and input a desired output(also an integer). It will specifically test to make sure that the output changes with the input. It has a very simple GUI that lets you control the boundaries of code generation, and present the user with those files that successfully generate the desired output, given the input. Later on I would like to have it track which ‘decisions’ are better for generating the desired output, and alter the way it generates code, so it can ‘learn’ as it generates code how better to generate code.

## Purpose
  This program is aimed solely towards teaching myself about artificial intelligence development and machine learning, and in the short term it will just be geared towards quickly generating code at a level similar in quality to human code, but quicker. It has GUI designed to make it easy to use, requires less comprehension of the code, and more utility. If done properly, the ability to auto-generate code within specified boundaries is an extremely appealing tool for any programmer.
  
  I wanted it to be as fast as possible, because the more useful it is, the more complex it will be. I’m having the compiler do much of the work for me in terms of determining whether the generated code is functional by having it run the generated code in RAM. 

## Practical Aplication
  I don’t know of any GUI equipped program designed to generate code for developers, aside from certain GUI creation IDE’s. This would be, hopefully, more useful than that. Instead of generating code for widgets, it would generate code for logical problems, potentially allowing for a deeper level of abstraction than what the programming language in question provides without actually ‘hiding’ the code, allowing for less abstraction if desired.
  
  How useful this is will change as it is developed. As far as I've gotten, it’s not super useful, since I'm only working with converting one integer into another – a simple calculator can do as much. But as the program grows more advanced, and hopefully to a lesser degree more complex, it will be able to generate code that is comparatively very time consuming for a human to generate.
  
  This will be useful on two fronts: One, code that is easy to understand and write, but simply takes a long time, and Two, code that is difficult to understand and therefore write, and therefore takes a lot of time. Being able to plug in logic instead of variables, and having a program that, in the fastest, and most efficient way possible, generates the code for you is exciting. If done in a way that is intelligible to human eyes, possibly revolutionary(and extensive).

  Obviously, the more complex the math/processing required to get the desired output, the more difficult it is to program an algorithm that is able to track and understand the function and purpose of the elements it is manipulating for that purpose. To simplify the logic, I had it only deal with integer input and output. This is temporary.

## Dirty Code
  I use the built-in `exec()` function to have the compiler assess the code for me. Since it doesn't return an input, per se, yet allows printing to sys.stdout, I swap out sys.stdout for the duration of the code's run, and also have a print statement before every return statement. Then the object that was sys.stdout while the program was running has the result of the code.
  
  I initially was concerned about the scalability - I couldn't figure out how to get all the processing done in RAM instead of on the disk, but when I discovered that I could use `exec()`, that fixed that.
  
  It's a little messy for now, but it will continue to progress as I work on it. Feel free to tinker, and download/run! Should be compatible with any operating system that has python 3. Just double-click the finalRunner, and it'll pop up.
