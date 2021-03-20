# NOTE: 
# the sympy method gives the sharpest chernoff bound 
# latex equation print needs ipython  
# think of some tests for timer class

from timer import Timer
import numpy as np
import sympy as sp
from sympy.abc import p,t,n,a
from sympy import *

# 1 
# manual chernoff bound (loose)
n = 100
a = 55
p = 0.5

mu = n*p
delta = (a/mu)-1
Pr_X_chernoff = np.exp(-((delta**2)/(2+delta)*mu))

print(f"mu: {mu}")
print(f"delta: {delta:.2f}")
print(f"Pr_X_chernoff: {Pr_X_chernoff:.3f}")


# 1
# sympy chernoff bound (sharp)
@Timer(name="decorator", text="Total time: {:0.4f} seconds")
def chernoff_min(f):   
    f1 = sp.diff(f, d)
    f1_eq = sp.Eq(f1, 0)
    chb =list (sp.solveset(f1_eq, d, sp.Reals))
    delta = chb[0]
    ans = f.subs({d:delta})
    print(f"Chernoff Min: {ans}")

n = 100
a = 55
p = .5
q = 1-p
d = sp.symbols(('d'))
f = ((q+p*sp.exp(d))**n) * (sp.exp(-d*a)) 

chernoff_min(f)


# 1
# check work with sympy
with Timer(text="run time: {:0.3f}"):
    f_prime = sp.diff((p+p*sp.exp(t))**n/sp.exp(t*a), t)
    solve_t = sp.solve(f_prime, t)
    print(solve_t)

print(Timer.timers)

p, t, n, a = symbols("p t n a")
f_prime = diff((p+p*exp(t))**n/exp(t*a), t)
solve_t = solve(f_prime, t)
solve_t

