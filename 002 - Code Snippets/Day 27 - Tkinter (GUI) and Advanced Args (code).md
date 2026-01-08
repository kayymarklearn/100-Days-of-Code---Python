2026-01-08 00:17

Status: incomplete

Tags: [[Day 27 - Tkinter, args, kwargs and GUI progs.]]

# Code snippets and Examples

```
# def add(*args):  
#     return sum(args)  
#  
# print(add(3, 5, 6))  
  
def calc(**kwargs):  
    for (key, value) in kwargs.items():  
        print(kwargs[key])  
  
calc(add=3, mul=5)  
  
class Car:  
    def __init__(self, **kwargs):  
        self.make = kwargs.get("make")  
        self.model = kwargs.get("model")  
  
car = Car(make="Nissan", model="GT-R")  
print(car.make)  
  
a = {'make': "Nissan", 'model': "Skyline"}  
  
for (key, value) in a.items():  
    print(a.get(key))  
  
print(a.get("hello")) # Returns None because the key does not exist
```

### Tkinter (GUI)
```from tkinter import *  
  
#Creating a new window and configurations  
window = Tk()  
window.title("Widget Examples")  
window.minsize(width=500, height=500)  
  
#Labels  
label = Label(text="This is old text")  
label.config(text="This is new text")  
label.pack()  
  
#Buttons  
def action():  
    print("Do something")  
  
#calls action() when pressed  
button = Button(text="Click Me", command=action)  
button.pack()  
  
#Entries  
entry = Entry(width=30)  
#Add some text to begin with  
entry.insert(END, string="Some text to begin with.")  
#Gets text in entry  
print(entry.get())  
entry.pack()  
  
#Text  
text = Text(height=5, width=30)  
#Puts cursor in textbox.  
text.focus()  
#Adds some text to begin with.  
text.insert(END, "Example of multi-line text entry.")  
#Get's current value in textbox at line 1, character 0  
print(text.get("1.0", END))  
text.pack()  
  
#Spinbox  
def spinbox_used():  
    #gets the current value in spinbox.  
    print(spinbox.get())  
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)  
spinbox.pack()  
  
#Scale  
#Called with current scale value.  
def scale_used(value):  
    print(value)  
scale = Scale(from_=0, to=100, command=scale_used)  
scale.pack()  
  
#Checkbutton  
def checkbutton_used():  
    #Prints 1 if On button checked, otherwise 0.  
    print(checked_state.get())  
#variable to hold on to checked state, 0 is off, 1 is on.  
checked_state = IntVar()  
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)  
checked_state.get()  
checkbutton.pack()  
  
#Radiobutton  
def radio_used():  
    print(radio_state.get())  
#Variable to hold on to which radio button value is checked.  
radio_state = IntVar()  
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)  
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)  
radiobutton1.pack()  
radiobutton2.pack()  
  
  
#Listbox  
def listbox_used(event):  
    # Gets current selection from listbox  
    print(listbox.get(listbox.curselection()))  
  
listbox = Listbox(height=4)  
fruits = ["Apple", "Pear", "Orange", "Banana"]  
for item in fruits:  
    listbox.insert(fruits.index(item), item)  
listbox.bind("<<ListboxSelect>>", listbox_used)  
listbox.pack()  
window.mainloop()

```

### Layout managers
```
from tkinter import *  
  
# Function to run when the button is clicked  
def button_clicked():  
    print("I got clicked")  
    my_label.config(text=input_field.get())  
  
window = Tk()  
window.title("My First GUI Program")  
window.minsize(width=500, height=300)  
  
# Label  
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))  
my_label.config(text="New Text")  
# my_label.pack(side="left")  
my_label.grid(row=0, column=0)  
  
# Button  
  
button = Button(text="Click Me", command=button_clicked)  
button.grid(column=1, row=1,columnspan=3)  
  
# Entry: Effectively Input  
  
input_field = Entry(width=40)  
input_field.insert(END, "Hello World")  
input_field.grid(row=2, column=2)  
  
  
window.mainloop()
```
