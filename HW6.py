import numpy as np

# 1 
n = 100
a = 55
p = 0.5

mu = n*p
delta = (a/mu)-1

Pr_X_chernoff = np.exp(-((delta**2)/(2+delta)*mu))
print(f"mu: {mu}")
print(f"delta: {delta:.2f}")
print(f"Pr_X_chernoff: {Pr_X_chernoff:.3f}")

n = 1000
a = 550
p = 0.5

mu = n*p
delta = (a/mu)-1

Pr_X_chernoff = np.exp(-((delta**2)/(2+delta)*mu))
print(f"mu: {mu}")
print(f"delta: {delta:.2f}")
print(f"Pr_X_chernoff: {Pr_X_chernoff:.3f}")
