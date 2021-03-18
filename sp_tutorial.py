#%%
import sympy

print(sympy.sqrt(3))
print(sympy.sqrt(8))

#%%
from sympy import symbols
x, y = symbols("x y")
expr = x +2*y
print(expr)
print(expr + 1)
print(expr - x)

# %%
from sympy import expand, factor
expanded_expr = expand(x*expr)
factor_expr = factor(expanded_expr)
print(expanded_expr)
print(factor_expr)

# %%
from sympy import *
x, t, z, n = symbols("x t z nu")
init_printing(use_unicode=True)

# %%
print(diff(sin(x)*exp(x), x))  # string
diff(sin(x)*exp(x), x)  # LaTeX

# %%
integrate(exp(x)*sin(x) + exp(x)*cos(x), x)

# %%
integrate(sin(x**2), (x, -oo, oo))

# %%
limit(sin(x)/x, x, 0)

# %%
solve(x**2 - 2, x)

# %%
y = Function("y")
dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))

# %%
Matrix([[1,2],[2,2]]).eigenvals()

# %%
latex(Integral(cos(x)**2, (x, 0, pi)))

# %%
a = (x+1)**2
b = x**2+ 2*x + 1
c = x**2 - 2*x + 1
print(simplify(a-b))
print(simplify(a-c))

# %%
a = cos(x)**2 - sin(x)**2
b = cos(2*x)
a.equals(b)

# %%
True ^ True
False ^ False
True ^ False

# %%
print(x + Rational(1,2))
print(x + 1/2)
# %%
