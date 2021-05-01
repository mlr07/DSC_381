from sympy import *
from IPython.display import display
import numpy as np

from symfit import Parameter, Variable, exp, parameters, variables, Fit
from symfit.core.objectives import LogLikelihood 
import numpy as np

theta = symbols("theta", positive=True)
n = symbols("n", positive=True)
x = Function("x")
i = symbols('i', positive=True)

L_log = n*log(theta) - theta*Sum(x(i), (i, 1, n))
display(L_log)

mle = Eq(diff(L_log, theta), 0).doit()
display(mle)

soln = solve(mle, theta)[0]
display(soln)

data = np.array([0.4, 2.4, 0.3, 1.7, 0.9])
theta_est = len(data) / sum(data)
print(theta_est)
print(len(data))
