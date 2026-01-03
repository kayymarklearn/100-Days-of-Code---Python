2026-01-03 09:40

Status: Incomplete

Tags:


# **Files**
> We can open a file using the python command (open(file, mode, buffering, encoding...))
> ```
> # Reading from files
> file = open("myfile.txt")
> contents = file.read()
> print(contents)
> file.close() # This closes the file from using system resources.
> # we can use the 'with' keyword to take care of opening and closing files for convenience
> with open("myfile.txt") as file:
> 	contents = file.read()
> 	print(contents)
>
># Writing to files
>When opened without a mode arguments, the file is set to read only, in other to write we use the w mode.
>with open("myfile.txt", mode='w') as file:
>	file.write("new text.") # Note that this overwrites previous file contents
># Append to files
># We can use the 'a' mode to append to files not overwrite them
>with open("myfile.txt", mode='a') as file:
>	file.write("\nNew text1") # this adds a new line and text to the file
># When you open a file in write mode and it does not exist, a newfile is created.
># The above also works when you use the append mode
> ```


# **Paths**
> Basically the hierarchy of files and directories in the file system.
> Normally starts from a root directory (C:/ on windows).
> Absolute file paths:
> 	These are file paths that start from the root directory `/home/username/helloworld.txt`
> Relative file paths:
> 	These are file paths that start from the working directory (represented by .) 
> 	`./workingdir/hello.txt`
> 	`../hello/file.txt` # .. here represents the parent dir of the current dir.
> 	```
> 	with open("/Users/me/apps/my_file.txt") as file: # Absolute file path
> 		content = file.read()
> 		print(content)
> 	with open("../newapps/my_new_file.txt") as file: # Relative file path
> 		content = file.read()
> 		print(content)
> 	```
## References
