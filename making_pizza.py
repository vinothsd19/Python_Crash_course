#import pizza
# we can also import a specific function from a module. Here's the general syntax for this approach:
#from pizza import make_pizza
# we can also give a function an alias by using the as keyword:
# from pizza import make_pizza as mp
# we can import every function in a module by using the asterisk (*) operator:
from pizza import *


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
If you use this kind of import statement to import 
an entire module named module_name.py, each function in the module is 
available through the following syntax:
--------------------------------------------------------------
module_name.function_name()
--------------------------------------------------------------
"""

