# %%

from scipy import integrate
import numpy as np

# quiz 4 by simulation form mykl and travis b
rng = np.random.default_rng()
n = 1000000
s = 3
lmb = 2
beta = 1/lmb

X1 = rng.exponential(beta,n)
X2 = rng.exponential(beta,n)
X3 = rng.exponential(beta,n)

#part 1
cdf_s = sum(i < s for i, j in zip(X1, X2) if i+j > s) / n
print(np.mean((X1 > s) & (X1 + X2 > s)))

print(f'cdf part 1 at {s}: {cdf_s}')

#part 2
cdf_s = sum(i+j < s for i, j, k in zip(X1, X2, X3) if i+j+k > s) / n
print(np.mean((X1 + X2 < s) & (X1 + X2 + X3 > s)))

print(f'cdf part 2 at {s}: {cdf_s}')


# lec 9.3, example 1 from tobor and james
# by simulation
n = 100000
mu = 3
sigma = 3

rng = np.random.default_rng()
X1 = rng.normal(mu, sigma, n)

print(np.mean((X1 > 2) & (X1 < 5)))

#%%
# by integration
mu=3
sig=3
i = lambda t: 1/(sig*sympy.sqrt(2*sympy.pi))*(sympy.exp(-(t-mu)**2/(2*sig**2)))
ans = integrate.quad(i,2,5)
print(ans[0])


# lec 9.6, example 1 from james
n=50
mu=0
var = 1/12
sig=sympy.sqrt(n*var)
low = -.3
high = .3
i = lambda t: 1/(sig*sympy.sqrt(2*sympy.pi))*(sympy.exp(-(t-mu)**2/(2*sig**2)))
ans = integrate.quad(i,low,high)
print(1-ans[0])

from sympy import symbols, Integral, Derivative, Eq, exp, sqrt, pi
x, t, mu, sigma = symbols("x t mu sigma")
# expr = 1 / (sqrt((2*pi*sigma)))
expr = 1/(sigma*sqrt(2*pi))*(exp(-(t-mu)**2/(2*sigma**2)))


# %%
