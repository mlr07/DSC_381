# %%
import numpy as np
import matplotlib.pyplot as plt


# 1 simulate tank captures
def sim_tank_cap(k: int, n: int, runs: int):
    rng = np.random.default_rng()
    tanks = np.arange(1, n+1)
    caps = [rng.choice(tanks, k, replace=False) for r in range(runs)]
    sample_max = np.array([np.max(cap) for cap in caps])
    sample_mean = np.array([np.mean(cap) for cap in caps])
    sample_sd = np.array([np.std(cap) for cap in caps])
    
    return sample_max, sample_mean, sample_sd

k = 5
n = 1000
runs = 10000

xmax, xbar, xsd = sim_tank_cap(k=k, n=n, runs=runs)


# 2 compute statistics
xbar2 = xbar*2
xbar3sd = xbar + 3*xsd
xmax_binom = ((k+1)/k) * xmax

xmax_mu = np.mean(xmax)
xmax_sd = np.std(xmax)

xbar2_mu = np.mean(xbar2)
xbar2_sd = np.std(xbar2)

xbar3sd_mu = np.mean(xbar3sd)
xbar3sd_sd = np.std(xbar3sd)

xmax_binom_mu = np.mean(xmax_binom)
xmax_binom_sd = np.std(xmax_binom)


# 3 plot it
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
ax = axes.ravel()

fig.suptitle(f"{runs} simulated {k} tank captures from {n} total tank serial numbers", fontsize=20)

ax[0].hist(xmax, k*5, density=False)
ax[0].axvline(n, color='red', linestyle='dashed', linewidth=2, label="N Tanks")
ax[0].axvline(xmax_mu, color='black', linestyle='dashed', linewidth=2, label="xmax_mu")
ax[0].set_xlabel(f"xmax")
ax[0].set_ylabel("simulation runs")
ax[0].set_title(f"xmax")
ax[0].text(200, 1250, f'xmax mu={xmax_mu:.3f}\nxmax sd={xmax_sd:.3f}')
ax[0].legend()

ax[1].hist(xbar2, k*5, density=False)
ax[1].axvline(n, color='red', linestyle='dashed', linewidth=2, label="N Tanks")
ax[1].axvline(xbar2_mu, color='black', linestyle='dashed', linewidth=2, label="xbar*2 mu")
ax[1].set_xlabel(f'xbar*2')
ax[1].set_ylabel("simulation runs")
ax[1].set_title(f"xbar*2")
ax[1].text(200, 900, f'xbar*2={xbar2_mu:.3f}\nxbar*2 sd={xbar2_sd:.3f}')
ax[1].legend()

ax[2].hist(xbar3sd, k*5, density=False)
ax[2].axvline(n, color='red', linestyle='dashed', linewidth=2, label="N Tanks")
ax[2].axvline(xbar3sd_mu, color='black', linestyle='dashed', linewidth=2, label="xbar+3d mu")
ax[2].set_xlabel(f'xbar + 3sd')
ax[2].set_ylabel("simulation runs")
ax[2].set_title(f"xbar + 3sd")
ax[2].text(200, 800, f'xbar+3sd mu={xbar3sd_mu:.3f}\nxbar+3sd sd={xbar3sd_sd:.3f}')
ax[2].legend()

ax[3].hist(xmax_binom, k*5, density=False)
ax[3].axvline(n, color='red', linestyle='dashed', linewidth=2, label="N Tanks")
ax[3].axvline(xmax_binom_mu, color='black', linestyle='dashed', linewidth=2, label="xmax binom")
ax[3].set_xlabel(f'xmax binom')
ax[3].set_ylabel("simulation runs")
ax[3].set_title(f"xmax binom")
ax[3].text(200, 1250, f'xmax binom mu={xmax_binom_mu:.3f}\nxmax binom sd={xmax_binom_sd:.3f}')
ax[3].legend()

fig.tight_layout()

# %%

# TODO compare k size with xmax binom