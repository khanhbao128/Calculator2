"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic_1 import *


def calculator():
    """Build a Prefix Calculator"""

    while True:

        calc_input = input("> ")
        tokens = calc_input.split(" ")
        float_tokens = []

        for i in range(1, len(tokens)):
            
            if tokens[i].isdigit():
                    tokens[i] = float(tokens[i])
                    float_tokens.append(tokens[i])
            else:
                print("Sorry thats not an valid input")


        if tokens[0] == "q":
            break

        elif tokens[0] == "+":
            print(add(float_tokens))

        elif tokens[0] == "-":
            print(subtract(float_tokens))

        elif tokens[0] == "*":
            print(multiply(float_tokens))

        elif len(float_tokens) > 2:

            if tokens[0] == "/":
                print(divide(float_tokens[0], float_tokens[1]))

            elif tokens[0] == "pow":
                print(power(tokens[1], tokens[2]))

            elif tokens[0] == "mod":
                print(mod(tokens[1], tokens[2]))
        
        elif tokens[0] == "square":
                print(square(tokens[1]))

        elif tokens[0] == "cube":
                print(cube(tokens[1]))

        else:
            print("Sorry, thats an invalid input")

calculator()

