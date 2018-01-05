"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while True:
    user_input = raw_input('> ')
    tokens = user_input.split()
    for i, token in enumerate(tokens):
        if i == 0:
            continue
        else:
            tokens[i] = float(token)

    if tokens[0] == 'q':
        break

    elif tokens[0] == '+':
        print add(tokens[1], tokens[2])

    elif tokens[0] == '-':
        print subtract(tokens[1], tokens[2])

    elif tokens[0] == '*':
        print multiply(tokens[1], tokens[2])

    elif tokens[0] == '/':
        print divide(tokens[1], tokens[2])

    elif tokens[0] == 'square':
        print square(tokens[1])

    elif tokens[0] == 'cube':
        print cube(tokens[1])

    elif tokens[0] == 'pow':
        print power(tokens[1], tokens[2])

    elif tokens[0] == 'mod':
        print mod(tokens[1], tokens[2])

    else:
        continue
