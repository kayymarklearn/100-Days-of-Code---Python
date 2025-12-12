2025-12-12 14:27

Status:

Tags:


# **How to fix errors in your code**
#### syntax
> Describe the problem
> Reproduce the bug

> Play computer: Go through code line by line and execute in  your head
> Fix Editor errors: any red lines or yellow lines by the code editor
> To solve console errors, You can search the parts of the code that are not specific to your code. Stackoverflow is a good resource.

### Use try/except blocks
> try:  
    age = int(input("How old are you?"))  
except ValueError:  
    print("You have typed in an invalid number. Try again with a numerical response")  
    age = int(input("How old are you?"))  
>      
if age > 18:  
    print(f"You can drive at age {age}.")

### Use print
> print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code. But during the loop it's difficult to see the intermediate values, that's a perfect example of how you can use print to expose those intermediate values and help you debug your code.

### Use a debugger
> Every code editor has  debuggers
> you can use pythontutor.com and thonny

	## Steps to use a debugger
	> 1. **Breakpoint** - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.
>
>	2. **Step Over** - This button will go through the execution of your code line by line and allow you>to view the intermediate values of your variables.
    >	
>	3. **Step Into** - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.
 > 	  
>	4. **Step Into My Code** - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.

## Tips
	a. Take a break (tackle the bug later)
	b. Ask a friend (preferably a developer or other learners)
	c. Run often (run your code after every few lines). Tackle multiple bugs one at a time
	d. Utilise stack Overflow. [Only when other avenues don't work.]
## References
