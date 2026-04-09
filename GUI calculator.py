"""
GUI Calculator - Tkinter-based graphical calculator.

This program creates a simple calculator GUI with basic arithmetic operations (+, -, *, /),
decimal point, clear, delete, square root, and equals. 
WARNING: Uses eval() for expression evaluation - for demo only, not production due to security risks.
Replace with safer parser like sympy for real use.

Author: [Your Name]
Date: [Current Date]
"""

from tkinter import *
import math

# Global variables
# operator: String to build the mathematical expression entered by user
operator = ""
# input_value: Tkinter StringVar to bind display Entry widget
input_value = StringVar()

def button_click(number):
    """
    Append a number or operator to the current expression.
    
    Args:
        number (str or int): Digit or operator to append.
    """
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def button_clear():
    """
    Clear the current expression and display.
    """
    global operator
    operator = ""
    input_value.set("")

def button_delete():
    """
    Delete the last character from the current expression.
    """
    global operator
    operator = operator[:-1] 
    input_value.set(operator)

def button_sqrt():
    """
    Append sqrt function start to the expression (requires manual closing paren or auto in equals).
    """
    global operator
    operator = operator + "math.sqrt("
    input_value.set(operator)

def button_equal():
    """
    Evaluate the current expression.
    - Auto-closes unbalanced parens.
    - Handles exceptions (e.g., syntax errors) by showing 'Error'.
    - Uses built-in eval() - WARNING: insecure for untrusted input.
    
    Updates display with result and clears expression.
    """
    global operator
    try:
        # Auto-balance parentheses if needed
        if operator.count("(") > operator.count(")"):
            operator += ")" * (operator.count("(") - operator.count(")"))
        
        result = str(eval(operator))
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

# Main application window
main = Tk()
main.title("Calculator")

# Display Entry widget
display_text = Entry(main, font=("arial", 20," bold"), textvariable=input_value, bd=15, insertwidth=2, 
                    bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

# Row 1 Buttons: numbers: 7, 8, 9 and addition signe (+)
btn_7 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="7", command=lambda:button_click(7))
btn_7.grid(row=1, column=0)

btn_8 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="8", command=lambda:button_click(8))
btn_8.grid(row=1, column=1)

btn_9 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="9", command=lambda:button_click(9))
btn_9.grid(row=1, column=2)
btn_add = Button(main, padx=12, bd=8, fg="black", bg="yellow",font=("arial",20,"bold"), text="+", command=lambda:button_click("+"))
btn_add.grid(row=1, column=3)

# Row 2 Buttons:  numbers: 4, 5, 6 and subtraction sign (-)
btn_4 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="4", command=lambda:button_click(4))
btn_4.grid(row=2, column=0)
btn_5 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="5", command=lambda:button_click(5))
btn_5.grid(row=2, column=1)
btn_6 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="6", command=lambda:button_click(6))
btn_6.grid(row=2, column=2)
btn_sub = Button(main, padx=16, bd=8, fg="black", bg="yellow", font=("arial",20,"bold"), text="-", command=lambda:button_click("-"))
btn_sub.grid(row=2, column=3)

# Row 3 Buttons:  numbers: 1, 2, 3 and multiplication sign (*)
btn_1 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="1", command=lambda:button_click(1))
btn_1.grid(row=3, column=0)
btn_2 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="2", command=lambda:button_click(2))
btn_2.grid(row=3, column=1)
btn_3 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="3", command=lambda:button_click(3))
btn_3.grid(row=3, column=2)
btn_mul = Button(main, padx=16, bd=8, fg="black",bg="yellow",font=("arial",20,"bold"), text="*", command=lambda:button_click("*"))
btn_mul.grid(row=3, column=3)

# Row 4 Buttons: number 0, decimal point (.), and clear button C
btn_0 = Button(main, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="0", command=lambda:button_click(0))
btn_0.grid(row=4, column=0)
btn_dot = Button(main, padx=19, bd=8, fg="black", font=("arial",20,"bold"), text=".", command=lambda:button_click("."))
btn_dot.grid(row=4, column=1)
btn_clear = Button(main, padx=14, bd=8, fg="black", bg="red", font=("arial",20,"bold"), text="C", command=button_clear)
btn_clear.grid(row=4, column=2)
btn_div = Button(main, padx=17, bd=8, fg="black",bg="yellow",font=("arial",20,"bold"), text="/", command=lambda:button_click("/"))
btn_div.grid(row=4, column=3)

# Row 5 Buttons: Del √ = (spans)
btn_del = Button(main, padx=16, bd=8, fg="black", bg="red", font=("arial",20,"bold"), text="Del", command=button_delete)  
btn_del.grid(row=5, column=0, columnspan=2)
btn_eq = Button(main, padx=16, bd=8, fg="black",bg="yellow",font=("arial",20,"bold"), text="=", command=button_equal)
btn_eq.grid(row=5, column=2)
btn_square = Button(main, padx=14, bd=8, fg="black",bg="yellow",font=("arial",20,"bold"), text="√", command=button_sqrt) 
btn_square.grid(row=5, column=3)

main.mainloop()

