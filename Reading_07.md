# Global Variables
In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

Example:

Input:

`x = "global"`

`def foo():`
    `print("x inside:", x)`


`foo()`
`print("x outside:", x)`

Output:

`x inside: global`  
`x outside: global`


# Nonlocal Variables
Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

We use `nonlocal` keywords to create nonlocal variables.

Example:

Input:

`def outer():`
    `x = "local"`

    `def inner():`
        `nonlocal x`
        `x = "nonlocal"`
        `print("inner:", x)`

    `inner()`
    `print("outer:", x)`


`outer()`

Output:

`inner: nonlocal`  
`outer: nonlocal`


