#
# keep relevant objects, data alive
# 
# main()
# 1. execute w/e code in main() as is directly in module's global namespace
# 2. if left in the if __name__ == __main__, module is importable
# 
# reason: to let ipython look at all defined variables inside main()
# 

'''
from my_functions import g

def f(x,y): return g(x,y)

def main():
    x=6
    y=7.5
    result = x+y

if __name__=="__main__": main()
'''

# 
# flat > nested
# 
# "flat is better than nested" (part of Zen of Python)
# functions, classes as decoupled, modular == easier to test, debug, use
# 

# 
# overcome fear of longer files
# 
# fewer files == few modules to reload == less jumping between editing files
# 
# longer files + high internal cohesion == useful, pythonic
# after iterating toward solution, refactor large --> small files
# 

#
##
###
### # 
### # # Advanced ipython features
### #
### 
##
#

#
# make classes friendly
# 
# console friendly string representation of object inspected
# user-defined classes require user to generate desired string output
#

class Message(object):
    def __init__(self, msg):
        self.msg=msg
    
    def __repr__(self):
        return "Message: '%s'" % self.msg

x = Message("I have a secret")

# # without the __repr__
# print x # <__main__.Message instance at ...>

# # with the __repr__
# print x # Message: I have a secret

# 
# profiles and configurations
# 
# editing ipython config: ~/.ipython/profile_default/ipython_config.py
# 
