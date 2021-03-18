# %%
import sympy
from sympy import symbols
from sympy import expand, factor
from sympy import *

import numpy as np

# %%
# print str
print(sympy.sqrt(3))
print(sympy.sqrt(8))

# make expressions
x, y = symbols("x y")
expr = x +2*y
print(expr)
print(expr + 1)
print(expr - x)

# expand and factor
expanded_expr = expand(x*expr)
factor_expr = factor(expanded_expr)
print(expanded_expr)
print(factor_expr)

# define expressions
x, t, z, n = symbols("x t z nu")

# set printing style
init_printing(use_unicode=True)
print(diff(sin(x)*exp(x), x))  # string
diff(sin(x)*exp(x), x)  # LaTeX

# integration
integrate(exp(x)*sin(x) + exp(x)*cos(x), x)
integrate(sin(x**2), (x, -oo, oo))

# limit
limit(sin(x)/x, x, 0)

# solve
solve(x**2 - 2, x)
y = Function("y")
dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))

# linalg
Matrix([[1,2],[2,2]]).eigenvals()

# output LaTeX
latex(Integral(cos(x)**2, (x, 0, pi)))

# simplify for equality
a = (x+1)**2
b = x**2+ 2*x + 1
c = x**2 - 2*x + 1
print(simplify(a-b))
print(simplify(a-c))

# eqaulity method
a = cos(x)**2 - sin(x)**2
b = cos(2*x)
a.equals(b)

# XOR bitwise exclusive
True ^ True
False ^ False
True ^ False

# rationals and floats
print(x + Rational(1,2))
print(x + 1/2)

# substitution
x, y, z = symbols("x y z")
expr = cos(x) + 1 # immutable
expr.subs(x, y)  # not copied in place
expr

# subsitution to build a symmetric function
expr = x**y
expr = expr.subs(y, expr)
print(expr.subs(y, x**x))

# substiution for controlled simplification
expr = sin(2*x) + cos(2*x)
expand_trig(expr)
expr.subs(2*sin(x)*cos(x), sin(2*x))

# multiple substitutions
expr = x**3 + 4*x*y - z
expr.subs([(x,2), (y,4), (z,0)])

# generate substitutions from list comp
expr = x**4 + 4*x**3 + 4*x**2 - 2*x + 3
replace = [(x**i, y**i) for i in range(5) if i % 2 == 0]
print(replace)
expr.subs(replace)

# convert strings to expressions
str_expr = "x**2 + 3*x - 1/2"
expr = sympify(str_expr)
expr.subs(x, 2)
# evaluate numerically
expr = sqrt(8)
expr
expr.evalf()

# control floating point precision
pi.evalf(50)

# evaluate with substitution
expr = cos(2*x)
expr.evalf(subs={x:2.4})

# evaluate with lambdify
a = np.arange(10)
expr = sin(x)
f = lambdify(x, expr, modules="numpy")
f(a)

# init best printer for environment
from sympy import init_printing
init_printing() 

# init interactive session
from sympy import init_session
init_session()

# print sympy object as string and srepr
x = symbols("x")
expr = Integral(sqrt(1/x), x)
print(str(expr))
print(srepr(expr))

# pretty print with unicode
pprint(expr, use_unicode=True)

# %%
p, t, n, a = symbols("p t n a")
f_prime = diff((p+p*exp(t))**n/exp(t*a), t)
solve_t = solve(f_prime, t)
solve_t