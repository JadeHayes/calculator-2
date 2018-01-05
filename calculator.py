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
        num = tokens[1:]
        print add(num)

    elif tokens[0] == '-':
        new = tokens[1:]
        print subtract(new)

    elif tokens[0] == '*':
        new = tokens[1:]
        print multiply(new)

    elif tokens[0] == '/':
        new = tokens[1:]
        print divide(new)

    elif tokens[0] == 'square':
        new = tokens[1:]
        print square(new)

    elif tokens[0] == 'cube':
        new = tokens[1:]
        print cube(new)

    elif tokens[0] == 'pow':
        new = tokens[1:]
        print power(new)

    elif tokens[0] == 'mod':
        new = tokens[1:]
        print mod(new)

    else:
        continue
