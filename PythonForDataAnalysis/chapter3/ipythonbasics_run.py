# # chapter 3 is related to using ipython IDE
# # as it's a 'execute-explore' flow (w AST)
# # vs 'edit-compile-run' flow of shell + text editor
# # https://docs.python.org/2/library/ast.html
# # http://www.quora.com/What-is-the-difference-between-IPython-and-Python

import numpy as np

data = {i:np.random.randn() for i in range(7)}
# print data
'''
{0: -1.2685700476508255,
 1: 0.7499336774965497,
 2: -1.6717797681135789,
 3: 0.5374705091193017,
 4: 1.108534434516849,
 5: 0.3940522159922,
 6: 0.9615865146145879}
'''

blist = [1,2,3]
# # ipython reads cmd prompt input as line of text
# # : checks '?' at EOL (before eval <--?)
# # http://stackoverflow.com/questions/9884764/how-does-ipythons-operator-actually-work
# # # # #
# # Note: 'b?' results in SyntaxError, not recognizing '?'
# # in ipython terminal
# # >>> from ipythonbasics import b
# # >>> blist?
# # Type:        list
# # String form: [1, 2, 3]
# # Length:      3
# # Docstring:
# # list() -> new empty list
# # list(iterable) -> new list initialized from iterable's items
# # 
# blist? # this breaks when running

def add_numbers(a,b):
    """
        Add two numbers together
        :returns: sum of args
    """
    return a+b
# add_numbers?
'''
In [3]: from ipythonbasics import add_numbers
In [4]: add_numbers?

Type:        function
String form: <function add_numbers at 0x1120c7758>
File:        /Users/kliang112/Documents/Projects_self/Pandas/PandasLearning/PythonForDataAnalysis/chapter3/ipythonbasics.py
Definition:  add_numbers(a, b)
Docstring:
Add two numbers together
:returns: sum of args
'''

# add_numbers?? # shows the source code

def f(x,y,z): return (x+y)/z
a,b,c = 5,6,7.5
# result = f(a,b,c); print result # 1.46666666667

