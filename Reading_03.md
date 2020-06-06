# Reading 03: FileIO & Exceptions

## What Is a File?

 - A file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

 ## There are three main parts of a file.

    1. Header: metadata about the contents of the file (file name, size, type, and so on)
    2.  Data: contents of the file as written by the creator or editor
    3.  End of file (EOF): special character that indicates the end of the file

## File Paths
When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

    1.  Folder Path: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)
    2.  File Name: the actual name of the file
    3.  Extension: the end of the file path pre-pended with a period (.) used to indicate the file type

## Line Endings

  - ASA standard states that line endings should use the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n). The ISO standard however allowed for either the CR+LF characters or just the LF character.

## Opening and Closing a File in Python

  - When you want to work with a file, the first thing to do is to open it. This is done by invoking the open() built-in function. open() has a single required argument that is the path to the file. open() has a single return, the file object.

  ## Python Exceptions: An Introduction

  A Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception. 

  ## Exceptions versus Syntax Errors

  `>>> print( 0 / 0 ))`
    `File "<stdin>", line 1`
   `print( 0 / 0 ))`
                  ^
`SyntaxError: invalid syntax`

- Syntax errors occur when the parser detects an incorrect statement. (Shown Above)

-  The arrow indicates where the parser ran into the syntax error. In this example, there was one bracket too many.

`>>> print( 0 / 0)`
`Traceback (most recent call last):`
  `File "<stdin>", line 1, in <module>`
`ZeroDivisionError: integer division or modulo by zero`

## Raising an Exception

- Use raise to force an exception:

`raise -------> Exception`

## The AssertionError Exception

  - Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. 

  Assert that a condition is met:

  `assert -----> Test if condition is True`

  ## The try and except Block: Handling Exceptions

  `try ----> run this code`

  `except ----> execute this code when there is an exception`

  ## The else Clause

  `try ----> run this code`

  `except ----> execute this code when there is an exception`

  `else ----> No exceptions? run this code`

  ## Cleaning Up After Using finally

   `try ----> run this code`

  `except ----> execute this code when there is an exception`

  `else ----> No exceptions? run this code`

  `finally ----> Always run this code`












