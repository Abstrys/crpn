# crpn - A simple command-line calculator

This is a simple [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
(RPN) calculator for use in a command-line terminal.

It's essentially a ground-up rewrite of my desktop calculator,
[NeRPN](https://github.com/Abstrys/NeRPN), which is still a neat example of a Swing Java application
and works well enough if you're looking for a graphical (but minimal) RPN calculator.

This version is written in pure Python and should run just about anywhere. It can be used over SSH
in a pure terminal environment, and of course, will use the colors and fonts you have set in your
terminal.


## How to use it

Install from source:

1. [Download the source](https://github.com/Abstrys/crpn/archive/main.zip) and unarchive it:

        cd ~/Downloads
        unzip crpn-main.zip

1. Go to the root of the directory just created:

        cd crpn-main

1. Make sure that you have `pep517` installed:

        pip install pep517

1. Then, run these commands to complete the installation:

        cd crpn
        python -m pep517.build .
        pip install dist/crpn-0.0.1.tar.gz

Running it:

1. Run it by running **`crpn`**. It will provide a few instructions and show you the stack, which
   will initially be empty:

        ===================================================
        crpn v.0.0.1 - a minimalist command-line calculator
        ===================================================
        
        Enter values on the stack, or the name of an operation or command.
        
        Type 'quit' or 'exit' to quit.  Type 'help' for help.
        
        Current stack:
        ------------------------
        ------------------------
        > 

1. Type values (either integer or floating-point) and press **Enter** to add them to the stack.

        > 10
        ------------------------
         0:   10
        ------------------------
        > 2
        ------------------------
         1:   10
         0:   2
        ------------------------

1. Type operations (`+`, `-`, `*`, `/`, `!`, `^`, `cos`, `abs`, etc.) to operate on stack members
   and see the results of the calculation.

        > ^
        ------------------------
         0:   100
        ------------------------

1. Type `quit` or `exit` to save the stack and quit.


## Other things to try

* Type `help commands` or `help operations` for a list of all current operations.

* Type `help` or `help <op_name>` to get general help or help for a specific operation at any time.

* Press **Enter** without entering a value to duplicate the final row on the stack.

* Type `del` or `del <n>` to delete stack row(s), or `clear` to clear the stack

* You can combine operations with `&&`. For example, to clear the stack and then quit, type:

        > clear && quit


## List of operations

(generated using `help operations`)

* 'abs' - Compute the absolute value of row 0.
* 'acos' - Compute the arccosine of row 0.
* 'add' - Add rows 0 and 1 together.
* 'asin' - Compute the arcsine of row 0.
* 'atan' - Compute the arctangent of row 0.
* 'cbrt' - cbrt
* 'ceil' - ceil
* 'clear' - Clear the stack.
* 'cos' - Compute the cosine of row 0.
* 'cosh' - Compute the hyperbolic cosine of row 0.
* 'deg' - deg
* 'del' - Delete row 0, or the row specified by the optional argument.
* 'div' - Divide row 1 by row 0.
* 'dup' - Duplicate row 0 and add it to the stack.
* 'e' - e
* 'en1' - en1
* 'eng' - eng
* 'exp' - exp
* 'expn1' - expn1
* 'fact' - Compute the factorial of row 0.
* 'fix' - fix
* 'floor' - floor
* 'help' - Print general help, or for a given operation.
* 'hyp' - hyp
* 'inv' - inv
* 'ln' - ln
* 'log' - log
* 'max' - max
* 'min' - min
* 'mult' - Multiply rows 0 and 1.
* 'neg' - neg
* 'pow' - pow
* 'quit' - Save the current state and quit.
* 'rad' - rad
* 'rand' - Add a random fractional value to the stack.
* 'root' - root
* 'rot' - rot
* 'sci' - sci
* 'sin' - Compute the sine of row 0.
* 'sinh' - Compute the hyperbolic sine of row 0.
* 'sqrt' - Compute the square root of row 0.
* 'std' - std
* 'subt' - Subtract row 0 from row 1.
* 'sum' - Sum all rows, or a given number of them, together.
* 'swap' - Swap rows 0 and 1, or row 0 with the one provided in the optional parameter.
* 'tan' - Compute the tangent of row 0.
* 'tanh' - Compute the hyperbolic tangent of row 0.

To get built-in help for any of these operations, type `help <op_name>`.


## License

This code is provided under the MIT license. You are free to use it for any purpose, but I assume no
liability and offer no warranty. See the
[LICENSE](https://github.com/Abstrys/crpn/blob/main/LICENSE) file for full details.

