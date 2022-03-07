from functools import partial
mod_checker = lambda x,mod=0 : partial( lambda y,x1: y % x1 == mod, x1=x )