def works_fine():
    a = 5
    b = 6
    assert(a + b == 11)

def throws_an_exception():
    a = 5
    b = 6
    assert(a + b == 10)

def calling_things():
    works_fine()
    throws_an_exception()

calling_things()

### # 
### # poor man's breakpoint
### # 
from IPython.core.debugger import Pdb

def set_trace():
    Pdb(color_scheme="Linux").set_trace(
        sys.getframe().f_back
    )

def debug(f, *args, **kwargs):
    pdb=Pdb(color_scheme="Linux")
    return pdb.runcall(f, *args, **kwargs)
