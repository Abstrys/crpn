#!/usr/bin/env python
# crpn - a minimalist command-line calculator
#
# Copyright © 2020, Eron Hennessey
#
# This code is provided under the terms of the MIT open source license. See the LICENSE file
# included with this repository for # details.

import sys
import math, random
import json

ID_TEXT = """
===================================================
crpn v.0.0.1 - a minimalist command-line calculator
===================================================
"""

HELP_TEXT = """
Enter values on the stack, or the name of an operation or command.

Type 'quit' or 'exit' to quit.  Type 'help' for help.
"""

CONST_MAP = {
    "E": math.e,
    "PI": math.pi,
    "TAU": math.tau,
}

OP_METHOD_MAP = {
    "!": "fact",
    "": "dup",
    "%": "mod",
    "*": "mult",
    "+": "add",
    "-": "subt",
    "/": "div",
    "^": "pow",
    "abs": "abs",
    "acos": "acos",
    "asin": "asin",
    "atan": "atan",
    "help": "help",
    "cbrt": "cbrt",
    "ceil": "ceil",
    "clear": "clear",
    "cos": "cos",
    "cosh": "cosh",
    "deg": "deg",
    "del": "delete",
    "dup": "dup",
    "e": "e",
    "en1": "en1",
    "eng": "eng",
    "exp": "exp",
    "expn1": "expn1",
    "fact": "fact",
    "fix": "fix",
    "floor": "floor",
    "hyp": "hyp",
    "inv": "inv",
    "ln": "ln",
    "log": "log",
    "max": "max",
    "min": "min",
    "neg": "neg",
    "pow": "pow",
    "rad": "rad",
    "rand": "rand",
    "root": "root",
    "rot": "rot",
    "sci": "sci",
    "sin": "sin",
    "sum": "sum",
    "sinh": "sinh",
    "sqrt": "sqrt",
    "std": "std",
    "swap": "swap",
    "tan": "tan",
    "tanh": "tanh",
}

DISPLAY_MODES = ("STD", "FIX", "SCI", "ENG") 
ANGLE_MODES = ("RAD", "DEG") 

class CRPN:
    """
    A class that contains an RPN calculator
    """
    def __init__(self):
        self.stack = []
        self.num_format = 'std'

    def process_input(self, user_input):
        # split any args from the input.
        cmd = args = None
        if ' ' in user_input:
            (cmd, args) = user_input.split(' ', 1)
        else:
            cmd = user_input
            args = None
        if cmd in OP_METHOD_MAP:
            method = getattr(self, 'op_' + OP_METHOD_MAP[cmd])
            method(args)
            return
        elif user_input in CONST_MAP:
            self.stack.append(CONST_MAP[user_input])
            return
        else:
            # is it an int or float?
            value = None
            try:
                value = int(user_input)
                self.stack.append(value)
                return
            except ValueError:
                pass

            value = float(user_input)
            self.stack.append(value)
            return

    def require_stack(self, n):
        cur_stack_size = len(self.stack)
        if cur_stack_size < n:
            err_str = "ERROR: Operation requires " + str(n)
            if n == 1:
                err_str += " argument; "
            else:
                err_str +=  " arguments; "
            err_str += "there "
            if cur_stack_size == 0:
                err_str += "are 0"
            elif cur_stack_size == 1:
                err_str += "is only 1"
            else:
                err_str += "are only " + str(cur_stack_size)
            err_str += " on the stack!"
            raise ValueError(err_str)

    def get_stack(self):
        return self.stack

    def print_stack(self):
        pass


    #
    # Operations
    #

    def op_abs(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        if type(val1) is int:
            self.stack.append(abs(val1))
        else:
            self.stack.append(math.fabs(val1))

    def op_acos(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.acos(val1))

    def op_asin(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.asin(val1))

    def op_atan(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.atan(val1))

    def op_add(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val1 + val2)

    def op_clear(self, args):
        self.stack = []

    def op_cos(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.cos(val1))

    def op_cosh(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.cosh(val1))

    def op_div(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val1 / val2)

    def op_deg(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.degrees(val1))

    def op_delete(self, args):
        self.require_stack(1)
        self.stack.pop()

    def op_dup(self, args):
        self.require_stack(1)
        self.stack.append(self.stack[-1])

    def op_fact(self, args):
        self.require_stack(1)
        if type(self.stack[-1]) is not int:
            raise ValueError("ERROR: The value in stack register 0 must be an integer!")
        val1 = self.stack.pop()
        self.stack.append(math.factorial(val1))

    def op_help(self, args):
        print(HELP_TEXT)

    def op_max(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(max([val1, val2]))

    def op_min(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(min([val1, val2]))

    def op_mult(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val1 * val2)

    def op_neg(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(-val1)

    def op_pow(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        if (type(val1) is int) and (type(val2) is int):
            self.stack.append(val2 ** val1)
        else:
            self.stack.append(math.pow(val2, val1))

    def op_rad(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.radians(val1))

    def op_rand(self, args):
        self.stack.append(random.random())

    def op_sin(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.sin(val1))

    def op_sinh(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.sinh(val1))

    def op_subt(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val1 - val2)


    def op_sum(self, args):
        """
        Add together all of the entries on the stack and push the result. Optionally, provide a
        number to restrict the number of stack entries summed.
        """
        sum = 0
        stack_levels = len(self.stack)
        if args != None:
            stack_levels = int(args[0])
        self.require_stack(stack_levels)
        for i in range(0, stack_levels):
            sum += self.stack.pop()
        self.stack.append(sum)


    def op_swap(self, args):
        self.require_stack(2)
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack += [val1, val2]

    def op_sqrt(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.sqrt(val1))

    def op_tan(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.tan(val1))

    def op_tanh(self, args):
        self.require_stack(1)
        val1 = self.stack.pop()
        self.stack.append(math.tanh(val1))


def main():
    app = CRPN()
    
    print(ID_TEXT + HELP_TEXT)
    print("Current stack:")
    while(True):
        # print the current stack
        stack_values = app.get_stack()
        stack_size = len(stack_values)
        print("-" * 24)
        for x in stack_values:
            stack_size -= 1
            print('%2s:   %s' % (stack_size, x))
        print("-" * 24)
        sys.stdout.write('> ')
        user_input = input()
        if user_input in ['quit', 'exit']:
            sys.exit(0)
        else:
            try:
                app.process_input(user_input)
            except ValueError as e:
                print(e)

