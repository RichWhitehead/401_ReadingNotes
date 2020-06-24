# Reading 08

# List Comprehension

List comprehensions are also more declarative than loops, which means they’re easier to read and understand. Loops require you to focus on how the list is created. You have to manually create an empty list, loop over the elements, and add each of them to the end of the list.   

# Examples

`x = [i for i in range(10)]`
`print x`

# This will give the output:
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`


Create a list using loops and list comprehension
For the next example, assume we want to create a list of squares. Start with an empty list.

# You can either use loops:

`squares = []`

`for x in range(10):`
    `squares.append(x**2)`
 
`print squares`
[`0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

# Or you can use list comprehensions to get the same result:
`squares = [x**2 for x in range(10)]`
`print squares`
`[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`  

Just remember the syntax: [ expression for item in list if conditional ]

Multiplying parts of a list
Multiply every part of a list by three and assign it to a new list.

`list1 = [3,4,5]`
 
`multiplied = [item*3 for item in list1] `
 
`print multiplied 
[9,12,15]`

Note how the item*3 multiplies each piece by 3.

Show the first letter of each word
We will take the first letter of each word and make a list out of it.

`listOfWords = ["this","is","a","list","of","words"]`

`items = [ word[0] for word in listOfWords ]`

`print items`
`The output should be: [‘t’, ‘i’, ‘a’, ‘l’, ‘o’, ‘w’]`

Lower/Upper case converter
Let’s show how easy you can convert lower case / upper case letters.

`[x.lower() for x in ["A","B","C"]]`
`['a', 'b', 'c']`

`[x.upper() for x in ["a","b","c"]]`
`['A', 'B', 'C']`  

Print numbers only from a given string


`string = "Hello 12345 World"`
`numbers = [x for x in string if x. ` `isdigit()]`


`['1', '2', '3', '4', '5']`
`Change x.isdigit() to x.isalpha()`


# Then create the filter by using list comprehension:

`fh = open("test.txt", "r")`

`result = [i for i in fh if "line3" in i]`

`print result`
`Output: [‘this is line3‘]`

Using list comprehension in functions
Now, let’s see how we can use list comprehension in functions.

# Create a function and name it double:

`def double(x):`
  `return x*2`

# If you now just print that function with a value in it, it should look like this:

`print double(10)`

`[double(x) for x in range(10)]`

`print double`
`[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]`

# You can put in conditions:

`[double(x) for x in range(10)`
 `if x%2==0]`
`[0, 4, 8, 12, 16]`

# You can add more arguments:

`[x+y for x in [10,30,50] for y in [20,40,60]]
[30, 50, 70, 50, 70, 90, 70, 90, 110]`
