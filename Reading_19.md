# Readings: Automation

## What is Regular Expressions?

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

## How are regular expression used?

RegEx can be used to check if a string contains the specified search pattern.

## Examples 

### RegEx Module

Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

`import re`

RegEx in Python
When you have imported the re module, you can start using regular expressions:

Example
Search the string to see if it starts with "The" and ends with "Spain":

`import re`

`txt = "The rain in Spain"`
`x = re.search("^The.*Spain$", txt)`

### RegEx Functions

The re module offers a set of functions that allows us to search a string for a match:

Function	Description

`findall	Returns a list containing all matches`
`search	Returns a Match object if there is a match anywhere in the string`
`split	Returns a list where the string has been split at each match`
`sub	Replaces one or many matches with a string`

### Metacharacters

Metacharacters are characters with a special meaning:


`[]	A set of characters	"[a-m]"	`
`\	Signals a special sequence (can also be used to escape special characters)	"\d"`	
`.	Any character (except newline character)	"he..o"	`
`^	Starts with	"^hello"`	
`$	Ends with	"world$"`
`*	Zero or more occurrences	"aix*"`	
`+	One or more occurrences	"aix+"`	
`{}	Exactly the specified number of occurrences	"al{2}"`
`|	Either or	"falls|stays"`
`()	Capture and group`

### The findall() Function

The findall() function returns a list containing all matches.

### The search() Function

The search() function searches the string for a match, and returns a Match object if there is a match.

### The split() Function

The split() function returns a list where the string has been split at each match.

### The sub() Function

The sub() function replaces the matches with the text of your choice.

### Match Object

A Match Object is an object containing information about the search and the result.



