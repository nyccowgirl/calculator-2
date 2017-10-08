"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from new_arithmetic import *


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
        output_file = open("results.txt", 'a')

        if len(math_list) < 2:
            print "Not enough inputs."
            continue

        result = 0

        if math_list[0] == "q":
            break
        elif math_list[0] == "+":
            result = add(math_list[1:])
        elif math_list[0] == "-":
            result = subtract(math_list[1:])
        elif math_list[0] == "*":
            result = multiply(math_list[1:])
        elif math_list[0] == "/":
            result = divide(math_list[1:])
        elif math_list[0] == "square":
            result = square(math_list[1:])
        elif math_list[0] == "cube":
            result = cube(math_list[1:])
        elif math_list[0] == "pow":
            result = power(math_list[1:])
        elif math_list[0] == "mod":
            result = mod(math_list[1:])
        elif math_list[0] == "x+":
            result - add_mult(math_list[1:])
        elif math_list[0] == "cubes+":
            result = add_cubes(math_list[1:])
        else:
            print "Those are not valid inputs. Note the math operator with spaces between that and the numbers."

        output_file.write(str(result) + "\n")

repl()
