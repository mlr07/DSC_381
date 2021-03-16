# NOTE: 
# the sympy method gives the sharpest chernoff bound 
# the latex like equation print might need jupyter/ipython
# check forms of the two given sympy equations

from timer import Timer
import numpy as np
import sympy as sp
from sympy.abc import p,t,n,a

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
    chb =list(sp.solveset(f1_eq, d, sp.Reals))
    delta = chb[0]
    ans = f.subs({d:delta})
    return ans

n = 100
a = 55
p = .5
q = 1-p
d = sp.symbols(('d'))
f = ((q+p*sp.exp(d))**n) * (sp.exp(-d*a)) 

Pr_X_sp = chernoff_min(f)
print(f"Pr_X_sp bound: {Pr_X_sp}")

n = 100
a = 60
p = .5
q = 1-p
d = sp.symbols(('d'))
f = ((q+p*sp.exp(d))**n) * (sp.exp(-d*a)) 

Pr_X_sp_2 = chernoff_min(f)
print(f"Pr_X_sp_2 bound: {Pr_X_sp_2}")

# 1
# check work with sympy
with Timer(text="run time: {:0.3f}"):
    f_prime = sp.diff((p+p*sp.exp(t))**n/sp.exp(t*a), t)
    solve_t = sp.solve(f_prime, t)
    print(solve_t)

print(Timer.timers)

