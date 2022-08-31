# Toy Programming Language #

This is a simple interpreter written in Python3 for a simple programming language. 

## Instructions to Run ##

To run the interpreter, use
``` 
python3 shell.py
```
to pass commands from a shell like interface. And, once inside the shell, use
```
toy> RUN("filename")
```
to pass commands from a file.

## Features ##

Some of the features supported by the programming language include:

Feature       | Example
:---:         | :---:
Math operators  | `4 + 2`, `4 - 2`, `4 * 2`, `4 / 2`, `4 ^ 2`
Floating point  and negative numbers | `4.2`, `-4`
Parantheses | `(4 + 1) * 3`
Variables | `VAR x = 3`
Comparison operators | `4 == 2`, `4 > 2`, `4 < 2`, `4 >= 2`, `4 <= 2`
Booleans | `TRUE`, `FALSE`
Logical operators | `4 == 4 AND 4 > 3`, `4 == 4 OR 4 > 3`, `NOT 4 == 4`
If statements | `IF <cond> THEN <expr>`
For statements | `FOR i = 0 TO 10 THEN <expr>`
While statements | `WHILE <cond> THEN <expr>`
Functions | `FUN add(a,b) -> a + b`
Strings | `"Hello world"`
Lists | `[1,2,3]`
Print | `PRINT("foo bar")`
Input | `INPUT_INT()`, `INPUT()`
Clear screen | `CLEAR()`, `CLS()`
Is Type | `IS_NUM(5)`, `IS_STR("foo")`, `IS_LIST([1,2])`
List operations | `APPEND([1,2,3], 4)`, `POP([1,2,3], 2)`, `EXTEND([1,2,3],[4,5,6])`
Error traceback calls

In addition to the these, the interpreter also recognises multiline statements separated by new lines or semicolons. It can take in input from a shell or a file.

## Other details ##

* `grammar.txt` contains the grammar rules for the programming language.
* `example.toy` is an example of code written in this language which you can run using the `RUN("example.toy")` command.



