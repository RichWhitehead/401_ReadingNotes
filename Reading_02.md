# Python Modules and Packages

Modular programming refers to the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules. Individual modules can then be cobbled together like building blocks to create a larger application.

There are several advantages to modularizing code in a large application:

  1. Simplicity: Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small portion of the problem. If you’re working on a single module, you’ll have a smaller problem domain to wrap your head around. This makes development easier and less error-prone.

  2. Maintainability: Modules are typically designed so that they enforce logical boundaries between different problem domains. If modules are written in a way that minimizes interdependency, there is decreased likelihood that modifications to a single module will have an impact on other parts of the program. This makes it more viable for a team of many programmers to work collaboratively on a large application.

  3. Reusability: Functionality defined in a single module can be easily reused by other parts of the application. This eliminates the need to duplicate code.

Scoping: Modules typically define a separate namespace, which helps avoid collisions between identifiers in different areas of a program.

Functions, modules and packages are all constructs in Python that promote code modularization.

# The Module Search Path

When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources:

The directory from which the input script was run or the current directory if the interpreter is being run interactively
The list of directories contained in the PYTHONPATH environment variable, if it is set.
An installation-dependent list of directories configured at the time Python is installed

`import mod`

# The import Statement

Module contents are made available to the caller with the import statement. The import statement takes many different forms.

`import <module_name>`

# The dir() Function

The built-in function dir() returns a list of defined names in a namespace. Without arguments, it produces an alphabetically sorted list of names in the current local symbol.

https://realpython.com/python-modules-packages/

https://docs.pytest.org/en/latest/

https://docs.pytest.org/en/latest/

https://www.geeksforgeeks.org/recursion/






