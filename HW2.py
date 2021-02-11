import math
import numpy as np
import pandas as pd


# HW2 Q9
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def combo_no_rep(n, r):
    return (factorial(n) / (factorial(r) * factorial(n-r)))


p = 1/(365)**2
r = 3
n = 50
k = combo_no_rep(n, r)

PrxA3 = math.exp(-(k*p))
print(f"PrxA3 = {PrxA3}")


# HW2 Q10
def Ihat(nxy):
    """
    arg: 2D matrix of observations for nx and ny (nxy)
    return: MI Ih(X, Y) --> approximated mutual information I for jointly distributed variables X,Y
    """
    n = nxy.sum()
    f = nxy/n
    fx = f.sum(axis=1).reshape(-1, 1)
    fy = f.sum(axis=0).reshape(1, -1)

    fx[fx == 0] = 0.01
    fy[fy == 0] = 0.01
    f[f == 0] = 0.01

    fxfy = np.dot(fx, fy)

    return (f * np.log(f/fxfy)).sum()


def sim(M, nxy):
    """
    args: number of simulations to run (M) and original 2D matrix of observations (nxy)
    return: Ihm(X, Y) 
    """
    n = nxy.sum()
    f = nxy/n

    fxh = f.sum(axis=1)
    fyh = f.sum(axis=0)

    nx = len(fxh)
    ny = len(fyh)

    Ihm = np.zeros(M)
    for m in range(len(Ihm)):
        xm = np.random.choice(range(1, nx + 1), n, True, fxh)
        ym = np.random.choice(range(1, ny + 1), n, True, fyh)
        nxym = pd.crosstab(xm, ym).fillna(0).to_numpy()
        Ihm[m] = Ihat(nxym)

    return Ihm


def Ihmstar(Ihm):
    """
    args: vector of M length with Ihm(X, Y) results
    return: Is at index of 95% confidence
    """
    M = len(Ihm)
    istar = int(round(M*0.95))
    Is = np.sort(Ihm)[istar]

    return Is


nxy = np.array(
    [[10, 9, 2],
     [10, 7, 2],
     [17, 11, 5],
     [22, 18, 7]]
)

Ih = Ihat(nxy)
print(f"Ih = {Ih}")

for i in range(10):
    M = 100
    Ihm = sim(M, nxy)
    Is = Ihmstar(Ihm)
    print(f"Is = {Is}")