# Reading 14 - Readings: Data Visualization

# What is MAthplotlib?

Matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

In matplotlib.pyplot various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes.

Importing your plot

`import matplotlib.pyplot as plt`
`plt.plot([1, 2, 3, 4])`
`plt.ylabel('some numbers')`
`plt.show()`

Formatting the style of your plot

`plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')`
`plt.axis([0, 6, 0, 20])`
`plt.show()`

Plotting with keyword strings

`data = {'a': np.arange(50),`
        `'c': np.random.randint(0, 50, 50),`
        `'d': np.random.randn(50)}`
`data['b'] = data['a'] + 10 * np.random.randn(50)`
`data['d'] = np.abs(data['d']) * 100`

`plt.scatter('a', 'b', c='c', s='d', data=data)`
`plt.xlabel('entry a')`
`plt.ylabel('entry b')`
`plt.show()`

Controlling line properties

Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; see matplotlib.lines.Line2D. There are several ways to set line properties

Use keyword args:

`plt.plot(x, y, linewidth=2.0)`
Use the setter methods of a Line2D instance. plot returns a list of Line2D objects; e.g., line1, line2 = plot(x1, y1, x2, y2). In the code below we will suppose that we have only one line so that the list returned is of length 1. We use tuple unpacking with line, to get the first element of that list:

`line, = plt.plot(x, y, '-')`
`line.set_antialiased(False)` # turn off antialiasing
Use the `setp()` command. The example below uses a MATLAB-style command to set multiple properties on a list of lines. setp works transparently with a list of objects or a single object. You can either use python keyword arguments or MATLAB-style string/value pairs:

`lines = plt.plot(x1, y1, x2, y2)`
# use keyword args
`plt.setp(lines, color='r', linewidth=2.0)`
# or MATLAB style string value pairs
`plt.setp(lines, 'color', 'r', 'linewidth', 2.0)`