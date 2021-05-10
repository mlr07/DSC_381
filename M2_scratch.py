import numpy as np
import scipy.stats as stats
from IPython.display import display
from sympy import *

def runner(runs:list=None, q:str=None) -> None:
    """
    Short function to track runs from Statkey.
    Args: 
        runs -> list of run results from statkey
        q -> string question number
    """

    if runs and len(runs) > 0:
        print(f"Q{q}: {len(runs)} run mean = {np.mean(runs):.4f}")
    else:
        print("No data")

theta = symbols("theta")
n = symbols("n")
alpha = symbols("alpha")
i = symbols('i')
x = Function("x")
gamma_ = Function("Gamma")