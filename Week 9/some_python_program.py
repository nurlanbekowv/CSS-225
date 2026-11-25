# Program description goes here
# A simple calculator with buttons. You click a number, an operator,
# another number, and = to see the answer.
# Updated on: 11/17/2026
# Updated by: Samat Toktonazarov, Christian Cagalitan, Josue, Arsen Tolobekov
#
# What we saw when testing:
# - Without root.mainloop() the window closes right away.
# - Without a .grid() line that button does not show up.
# - Dividing by 0 or typing letters makes the program crash.
#
# Document what the following lines of code do here
# Load tkinter, which makes windows and buttons.
from tkinter import *

# Make the main window.
root = Tk()

# Set the window title.
root.title("Simple Calculator")

# Document what the following lines of code do here
# Make the display box where numbers show up and place it at the top.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Document what the following lines of code do here
# Runs when a number is clicked. Adds the number to the end of the display.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Document what the following lines of code do here
# Runs when Clear is clicked. Empties the display.
def button_clear():
    e.delete(0, END)

# Document what the following lines of code do here
# Runs when + - * or / is clicked. Saves the first number and the
# operator, then empties the display for the second number.
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# Document what the following lines of code do here
# Runs when = is clicked. Does the math and shows the answer.
# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    second_number = e.get()                          # get the second number
    e.delete(0, END)                                 # empty the display
    if num_operator == '+':                          # if plus
        e.insert(0, f_num + int(second_number))      # add
    elif num_operator == '*':                        # if times
        e.insert(0, f_num * int(second_number))      # multiply
    elif num_operator == '/':                        # if divide
        e.insert(0, f_num / int(second_number))      # divide
    elif num_operator == '-':                        # if minus
        e.insert(0, f_num - int(second_number))      # subtract
    else:                                            # anything else
        e.insert(0, "Invalid!!!")                    # show an error

# Document what the following lines of code do here
# Make the number buttons, the + button, the = button and the Clear button.
# command tells each button which function to run when clicked.
#
# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Document what the following lines of code do here
# Make the - * and / buttons.
# See the description of a Lambda function above
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Document what the following lines of code do here
# Place each button in its row and column on the window.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Document what the following line of code do here
# Keep the window open and wait for clicks.
root.mainloop()
