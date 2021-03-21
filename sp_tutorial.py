# %%
import sympy
from sympy import symbols
from sympy import expand, factor
from sympy import *

import numpy as np

# %%
### INTRO ###
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

### GOTCHAS ###
# simplify for equality
a = (x+1)**2
b = x**2+ 2*x + 1
c = x**2 - 2*x + 1
print(simplify(a-b))
print(simplify(a-c))

# equality method
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

### BASIC OPERATIONS ###
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

### PRINTING ###
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

### SIMPLIFICATION ###
# simplify
x, y, z = symbols("x y z")
init_printing(use_unicode=True)

simplify(sin(x)**2 + cos(x)**2)
simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
simplify(gamma(x) / gamma(x-2)) # gamma function for complex factorials

# simplify pitfalls
expr = x**2 + 2*x + 1  # want factored form
simplify(expr)  # chooses simplest form
factor(expr)   # apply specific simplification

# expand polynomial/rational function
expand((x + 1)**2)
expand((x + 2)*(x - 3))
expand((x + 1)*(x - 2) - x*(x - 1))  # expanded terms cancel

# factor polynomial/rational function
factor(x**3 - x**2 + x - 1)
factor(x**2*z + 4*x*y*z + 4*y**2*z)

# factor list
factor_list(x**2*z + 4*x*y*z + 4*y**2*z)

# expand and factor
expr = (cos(x) + sin(x))**2
expand(expr)
factor(expr)

# collect powers into common terms
expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
expr_coll = collect(expr, x)
expr_coll

# collect specific coefficients
expr_coll.coeff(x, 2)

# cancel rational functions to canonical q/p
cancel((x**2 + 2*x + 1) / (x**2 + x))
expr = 1/x + (3*x/2 - 2)/(x - 4)
cancel(expr)

# cancel and factor rational function
expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
cancel(expr)
factor(expr)

# partial fraction decomposition with apart
x = symbols("x")
expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
expr
apart(expr)

### TRIG ###
# trig simplification
cos(acos(x))
asin(1)

# trigsimp
trigsimp(sin(x)**2  + cos(x)**2)
trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)
trigsimp(cosh(x)**2 + sinh(x)**2)

# expand_trig
x, y = symbols("x y")
expand_trig(sin(x+y))
expand_trig(tan(2*x))

# reverse trig identities
trigsimp(sin(x)*cos(y) + sin(y)*cos(x))

### POWERS ###
# symbol assumptions
x, y = symbols("x y", positive=True)
a, b = symbols("a b", real=True)
z, t, c = symbols("z t c")

# powsimp
powsimp(x**a*x**b)  # pow idnty 1
powsimp(x**a*y**a)  # pow idnty 2
powsimp(t**c*z**c)  # not valid
powsimp(t**c*z**c, force=True)  # force simp

# auto powsimp
(z*t)**2
sqrt(x*y)

# expand power exp and base
expand_power_exp(x**(a + b))
expand_power_base((x*y)**a)
expand_power_base((z*t)**c) # not valid
expand_power_base((z*t)**c, force=True) # force expand

# auto expand exp
x**2*x**3

# powdenest
powdenest((x**a)**b)  # pow idnty 3
powdenest((z**a)**b)  # not valid
powdenest((z**a)**b, force=True)  # force it

### EXP AND LOG ###
# log asssumptions
x, y = symbols("x y", positive=True)
n = symbols("n", real=True)
z, t = symbols("z t")

# expand log
expand_log(log(x*y))  # log idnty 1
expand_log(log(x/y))  # log idnty 1/2
expand_log(log(x**2))  # log idnty 2
expand_log(log(x**n))  # log idnty 2
expand_log(log(z*t))  # not valid
expand_log(log(z*t), force=True)  # force it

# combine log
logcombine(log(x) + log(y))
logcombine(log(x) - log(y))
logcombine(n*log(x) + log(y))

# exp
expand_log(log(exp(x)))
logcombine(log(exp(x)))

### CALCULUS ###
# derivatives with diff
x, y, z = symbols("x y z")
diff(cos(x))
diff(exp(x**2), x)

# higher order diff
diff(x**4, x, x, x)
diff(x**4, x, 3)

expr = exp(x*y*z)
diff(expr, x, y, y, z, z, z, z)

# diff as a method
expr.diff(x, y, 2, z, 4)

# unevaluated derivative
Derivative(expr, x, y, y, z, 4)

# higher order derivative from tuple
m, n, a, b = symbols("m n a b")
expr = (a*x + b)**m
expr.diff((x, n))

# indefinate integral
integrate(sin(x), x)  # primitive anitderivative
integrate(cos(x), x)  # primitive antiderivative

# definate integral
integrate(sin(x), (x, 0, 1))
integrate(cos(x), (x, 0, 1))
expr = Integral(exp(-x), (x, 0, oo))
expr.doit()

# double integral
expr = Integral(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
expr.doit()

# undefined integral
expr = integrate(x**x, x)
expr

# unevaluated integral
expr = Integral(log(x)**2, x)
expr.doit()

# evaluate a hard integral
expr = Integral(sin(x**2), x)
expr.doit()
expr = Integral(cos(x**2), x)
expr.doit()

# piecewise integral
expr = Integral(x**y*exp(-x), (x, 0, oo))
expr.doit()

# limits
limit(sin(x)/x, x, 0)

# limits for singularity
expr = x**2/exp(x)
expr.subs(x, oo)
limit(expr, x, oo)

# unevaluated limit
expr = Limit((cos(x)-1)/x, x, 0)
expr.doit()

# evaluate limit at one side
limit(1/x, x, 0, "+")
limit(1/x, x, 0, "-")

# series expansion
expr = exp(sin(x))
expr.series(x, 0, 4).removeO()  # remove O

# finite difference
f, g = symbols("f g", cls=Function)
differentiate_finite(f(x)*g(x))

f = Function("f")
dfdx = f(x).diff(x)
dfdx.as_finite_difference()

### SOLVERS ###
# apply equalities to eqns
x, y, z = symbols("x y z")

Eq(x**2 - 1, 1)
solveset(Eq(x**2, 1), x)

solveset(Eq(x**2 - 1, 0), x)
solveset(x**2 - 1, x)  # eqaul to zero assumed

# solving functions with algebra
solveset(x**2 - x, x)
solveset(x - x, x, domain=S.Reals)
solveset(sin(x) - 1, x, domain=S.Reals)

# no solution
solveset(exp(x), x)  # no soln
solveset(cos(x) - x, x)  # can't find soln

# solve system of linear equations
linsolve([x + y + 1, x + y + 2*z - 3], (x,y,z))  # list of eqns
linsolve(Matrix(([1,1,1,1], [1,1,2,3])), (x,y,z))  # augmented matrix

# A*x = b form
M = Matrix(((1,1,1,1), (1,1,2,3)))
system = A, b = M[:, :-1], M[:, -1]
linsolve(system, (x,y,z))  

# %%
# solve differential equation
f, g = symbols("f g", cls=Function)
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
diffeq
dsolve(diffeq, f(x))

dsolve(f(x).diff(x)*(1-sin(f(x)))-1, f(x))