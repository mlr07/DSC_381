# %%
import numpy as np
import matplotlib.pyplot as plt


def sim_tank_cap(k: int, n: int, runs: int):
    rng = np.random.default_rng()
    tanks = np.arange(1, n+1)
    return [np.max(rng.choice(tanks, k, replace=False)) for r in range(runs)]


k = 5
n = 100
runs = 10000

Xmax_arr = sim_tank_cap(k=k, n=n, runs=runs)
Xmax_mu = np.mean(Xmax_arr)
Xmax_sigma = np.std(Xmax_arr)

# %%
fig, ax = plt.subplots()

ax.hist(Xmax_arr, k*5, density=False)
ax.axvline(n, color='red', linestyle='dashed', linewidth=2, label="N Tanks")
ax.axvline(Xmax_mu, color='black', linestyle='dashed', linewidth=2, label="Xmax_mu")
ax.set_xlabel(f'Max serial number from {k} captured tanks')
ax.set_ylabel("simulation runs")
ax.set_title(f"{runs} simulated {k} tank captures from {n} N tanks")
ax.text(40, 1250, f'Xmax_mu={Xmax_mu:.3f}\nXmax_sigma={Xmax_sigma:.3f}')
ax.legend()
fig.tight_layout()
plt.show()
