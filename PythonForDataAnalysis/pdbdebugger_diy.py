# # 
# # how to use:
# # ----------
# # import this module, methods
# # run module normally using %run
# # 
# # in ipython: >>> debug(_func_name_, *_args_, **_kwargs_)
# # 
# # 

from IPython.core.debugger import Pdb

def set_trace():
    Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)

def debug(f, *args, **kwargs):
    pdb = Pdb(color_scheme='Linux')
    return pdb.runcall(f, *args, **kwargs)
