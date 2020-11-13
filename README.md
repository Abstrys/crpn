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

1. You can also press **Enter** without entering a value to repeat the first value on the stack,
   type `del` to delete stack entries, `clear` to clear the stack, `swap` to swap the first two
   entries on the stack, and many more operations.

1. You can type `help` to get help, or type `quit` or `exit` when you're ready to quit.


## License

This code is provided under the MIT license. You are free to use it for any purpose, but I assume no
liability and offer no warranty. See the
[LICENSE](https://github.com/Abstrys/crpn/blob/main/LICENSE) file for full details.

