# %%
from sympy import *
from IPython.display import display
import numpy as np

from symfit import Parameter, Variable, exp, parameters, variables, Fit
from symfit.core.objectives import LogLikelihood 
import numpy as np

# %%
# symfit example
data = np.array([14, 17, 27, 18, 12, 8, 22, 13, 19, 12])

# Define the model
theta = Parameter('theta')
x = Variable('x')
model = (1 / (theta)) * x *  exp(-x / theta)

# fit
fit = Fit(model, data, objective=LogLikelihood)
fit_result = fit.execute()
print(fit_result.__str__())

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
# build log likelihood for theta
L_log_theta = expand_log(log((theta+1)**n))+theta*Sum(log(X(i)), (i, 1, n))
display(L_log_theta)

# differentiate and set equal to zero
mle = Eq(diff(L_log_theta, theta), 0).doit()
display(mle)

# solve for theta
soln = solve(mle, theta)[0]
display(soln)

# 2nd derivative test for max
mle_max = diff(L_log_theta, theta, 2)
display(mle_max)

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
# 9 find mle for theta and estimate with given data
theta = symbols("theta", positive=True)  # param, unsure on number type
n = symbols("n", positive=True)  # n random values
x = Function("x")  # random value as a func
i = symbols('i', positive=True)  # index

L_log = -2*n*log(theta) + Sum(log(x(i)), (i, 1, n)) - 1/theta*Sum(x(i), (i, 1, n))
display(L_log)

mle = Eq(diff(L_log, theta), 0).doit()
display(mle)

soln = solve(mle, theta)[0]
display(soln)

# estimate theta with mle and data
data = [2.85, 11.07, 3.84, 7.92, 5.83, 8.81, 12.33, 9.74, 3.38, 21.91]
n = len(data)
theta_est = sum(data) / (2*n)

# 9 with symfit
data = np.array([2.85, 11.07, 3.84, 7.92, 5.83, 8.81, 12.33, 9.74, 3.38, 21.91])

# Define the model
theta = Parameter('theta')
x = Variable('x')
model = (1 / theta**2) * x * exp(-x / theta)

# fit
fit = Fit(model, data, objective=LogLikelihood)
fit_result = fit.execute()

print(f"theta mle estimate with symfit: {fit_result.value(theta):.3f}")
print(f"theta mle estimate with sympy: {theta_est:.3f}")
# print(f"dist to 3 = {theta_est-3:.3f}")
# print(f"dist to 6 = {6-theta_est:.3f}")

# %%
# 10 find theta**2 by invariance with theta mle
theta_sq_est = (theta_est)**2
print(f"estimate with theta**2 mle: {theta_sq_est:.3f}")

# %%
# 11 with sympy
theta = symbols("theta", positive=True)
n = symbols("n", positive=True)
i = symbols('i', positive=True)
alpha = symbols("alpha", positive=True)
x = Function("x")
gamma_ = Function("Gamma")

L_log = -n*log(gamma_(alpha)) - n*alpha*log(theta) + (alpha-1)*Sum(log(x(i)), (i, 1, n)) - (1/theta)*Sum(x(i), (i, 1, n))
display(L_log)

mle = Eq(diff(L_log, theta), 0).doit()
display(mle)

soln = solve(mle, theta)[0]
display(soln)

data = np.array([17.47, 9.1, 13.74, 30.68, 41.66, 16.53, 43.44, 21.18, 43.16, 74.17])
n = len(data)
a = 3.7
theta_est = np.sum(data) / (a*n)

# 11 with symfit
from math import gamma
theta = Parameter('theta')
x = Variable('x')
alpha = Variable("alpha")
gamma_rv = gamma(a)
model = (1 / (gamma_rv*theta**a)) * x**(a-1) * exp(-x / theta)

fit = Fit(model, data, objective=LogLikelihood)
fit_result = fit.execute()

print(f"theta mle estimate with sympy: {theta_est:.3f}")
print(f"theta mle estimate with symfit: {fit_result.value(theta):.3f}")

# %%
# 12 find sqrt(theta) by invariance with theta mle
theta_sqrt_mle = np.sqrt(theta_est)
print(f"estimate with sqrt(theta) mle: {theta_sqrt_mle:.3f}")

# %%
# 13 graphical mle
# the mle theta is the sample max...
data = np.array([0.7, 0.83, 2.39, 1.98, 3.76, 2.24, 12.44, 7.34, 2.76, 14.03])

Xmax = np.max(data)
theta = (Xmax-1)/2
print(f"theta from bounds: {theta}")

# 
var = (2*theta+1)**2 / 12
alt = (Xmax)**2 / 12

print(f"var from theta: {var}")
print(f"alt var: {alt}")
