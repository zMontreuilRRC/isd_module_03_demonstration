"""
Author: Zacharie Montreuil
Description: Introduction to Python Control Structures
Date: 30 January 2024
"""

# Sequential, Selection, Iteration
# SELECTION
# Conditionals
# if something is the case, do one thing, otherwise, do another thing

#assignment
age = 20

#comparison evaluation
if age == 0:
    print("Not born yet")
    print("This is a weird way to indicate that")
    print("Why are you still here?")
elif age < 13: #"else if" (evaluate this if the previous evaluation was false)
    print("Child")
else:
    print("None of the specified ages")

# nested conditionals

x_pos = 0
y_pos = 0

y_sign = ""
x_sign = ""

if x_pos > 0:
    x_sign = "positive"
elif x_pos < 0:
    x_sign = "negative"
else: 
    x_sign = "zero"

if y_pos > 0:
    y_sign = "positive"
elif y_pos < 0:
    y_sign = "negative"
else: 
    y_sign = "zero"

print(f"X is {x_sign} and y is {y_sign}")

# ==: Equality (e.g. 0 == 0 == True)
# !: NOT operator ( 0 != 1 == True)
if x_pos != y_pos:
    print("x and y positions are not equal")

# LOGICAL OPERATORS: and, or, not
    
if x_pos > y_pos and y_pos > 0 and y_pos == 0 and y_pos < 0:
    print("x is greater than y -- y is greater than zero")

# this will always evaluate to true
if x_pos == 0:
    if (y_pos > 0 or y_pos < 0):
        print("X is zero or Y is not zero")

# Ternary expressions
my_num = 12
if my_num % 2 == 0:
    print("even")
else: 
    print("odd")

#ternary: assign the value of "result" based on the conditional
result = "even" if my_num % 2 == 0 else "odd"

# in
fruits = ['apple', 'banana', 'kiwi', '3']

print('banana' in fruits) #output true
print(3 in fruits) #output false

sentence = "this was sent."
print("sent " in sentence)
