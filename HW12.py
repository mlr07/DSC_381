# %%
from sympy import *
from IPython.display import display

# %%
# mle for bern(p), no log used --> from PSU 415 sec1.2
x = IndexedBase('x')
i = symbols('i', positive=True)
n = symbols('n', positive=True)
p = symbols('p', positive=True)

mle = solve(Eq(diff(Product(p**x[i]*(1 - p)**(1 - x[i]), (i, 1, n)), p), 0).doit(), p)[1]
display(mle)

# %%
# 1 find mle for theta
theta = symbols("theta", positive=True)  # param, unsure on number type
n = symbols("n", positive=True)  # n random values
x = symbols("x", positive=True)  # random value
i = symbols('i', positive=True)  # index

# build log likelihood for theta
L_log_theta = expand_log(log((theta+1)**n))+theta*log(Sum(Indexed("x", i), (i, 1, n)))
display(L_log_theta)

# differentiate and set equal to zero
mle = Eq(diff(L_log_theta, theta), 0).doit()
display(mle)

# solve for theta
soln = solve(mle, theta)[0]
display(soln)

# %%
# 2 find mle for norm(mu, sigma**2)
theta1 = symbols("theta_1", positive=True)
theta2 = symbols("theta_2", positive=True)
n = symbols("n", positive=True)
i = symbols('i', positive=True)
x = Function("x")
L = Function("L")

L_log = -(n/2)*log(theta2)-(n/2)*log(2*pi)-(1/(2*theta2))*Sum((x(i)-theta1)**2, (i, 1, n))
display(L_log)

mle = Eq(diff(L_log, theta1), 0).doit()
display(mle)

soln = solve(mle, theta1)
# display(soln)

mle2 = Eq(diff(L_log, theta2), 0).doit()
display(mle2)

soln2 = solve(mle2, theta2)[0]
# display(soln2)

# %%
