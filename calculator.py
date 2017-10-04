"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *



# Your code goes here
def get_input():
    """ Get input from user on mathmetic operations and numbers """
    math_inputs = raw_input("> ")
    return math_inputs

def tokenize_input(math_inputs):
    """ Split user input into list """
    tokens = math_inputs.split(" ")
    for i in range(len(tokens)):
        if tokens[i].isdigit():
            tokens[i] = float(tokens[i])
    return tokens

def repl():
    """ Execute calculator based on user inputs of variable and numbers """
    while True:
        math_list = tokenize_input(get_input())

        if math_list[0] == "q":
            break
        elif math_list[0] == "+":
            print add(math_list[1], math_list[2])
        elif math_list[0] == "-":
            print subtract(math_list[1], math_list[2])
        elif math_list[0] == "*":
            print multiply(math_list[1], math_list[2])
        elif math_list[0] == "/":
            print divide(math_list[1], math_list[2])
        elif math_list[0] == "square":
            print square(math_list[1])
        elif math_list[0] == "cube":
            print cube(math_list[1])
        elif math_list[0] == "pow":
            print power(math_list[1], math_list[2])
        elif math_list[0] == "mod":
            print mod(math_list[1], math_list[2])
        elif math_list[0] == "x+":
            print add_mult(math_list[1], math_list[2], math_list[3])
        elif math_list[0] == "cubes+":
            print add_cubes(math_list[1], math_list[2])
        else:
            print "Those are not valid inputs. Note the math operator with spaces between that and the numbers."

repl()
