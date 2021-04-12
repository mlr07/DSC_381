import numpy as np
import matplotlib.pyplot as plt

### Part 1 by simulation ###
# exp(lambda) pdf ~ lmbda*exp(-lmbda*x) --> integrate(lmbda*exp(-lmbda*x)) = cdf
# find Pr( X1 < s, X1 + X2 > s) --> Pr(X1 < s < X1+X2) --> cdf

# set up simulation
rng = np.random.default_rng(42)  # construct random generator
n = 10000000  # trials
s = 3  # given random variable
lmbda = 2  # rate parameter
beta = 1/lmbda  # scale parameter, inverse of lmbda

# run simulation and generate random exponential samples
X1 = rng.exponential(beta, n)  
X2 = rng.exponential(beta, n)
X3 = rng.exponential(beta, n)

# search data for conditions of cdf
# equivalent to integrating pdf to get cdf
Pr1 = np.mean((X1 < s) & (X1+X2 > s))
print(np.mean(X1 < s))
print(np.mean(X1+X2 > s))
print(f"Pr(X1 < s < X1+X2) = {Pr1:.4f}")

### Part 2 by simulation ###
# find Pr(X1+X2 < s, X1+X2+X3 > s) --> Pr(X1+X2 < s < X1+X2+X3)

# reuse most of the objects above

# search data for conditions of cdf
Pr2 = np.mean((X1+X2 < s) & (X1+X2+X3 > s))
print(np.mean(X1+X2 < s))
print(np.mean(X1+X2+X3 > s))
print(f"Pr(X1+X2 < s < X1+X2+X3) = {Pr2:.4f}")

### Plot random exponentials for fun ###
fig, axs = plt.subplots(3)
axs[0].hist(X1, bins=100)
axs[1].hist(X2, bins=100)
axs[2].hist(X2, bins=100)
axs[0].set_title("X1")
axs[1].set_title("X2")
axs[2].set_title("X3")
fig.tight_layout()
plt.show()
