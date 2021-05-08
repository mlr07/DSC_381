# stats portion
# inference --> HW4
# simulation --> HW9
# theoretical distn --> HW10
# chi**2 and ANOVA --> HW11
# MLE --> HW12
# exp families --> HW13
# QZ5 and QZ6

# %%
import pandas as pd
import numpy as np
import scipy.stats as stats
from statistics import mean
from IPython.display import Latex, display

def runner(runs:list=None, q:str=None) -> None:
    """
    Short function to track runs from Statkey.
    Args: 
        runs -> list of run results from statkey
        q -> string question number
    """

    if runs and len(runs) > 0:
        print(f"Q{q}: {len(runs)} run mean = {mean(runs):.4f}")
    else:
        print("No data")
# %%
# 1 90%CI for pop sd from atlanta commutes: CI for single param
runner([23.574-17.846, 23.643-17.814, 23.632-17.848, 23.616-17.884], 1)

# 2 proportion of blackberry users from CellPhoneTypes: one category descriptive
# Type, Frequency
# Android, 458
# iPhone, 437
# Blackberry, 141
# Std. Cell Phone, 924
# No Cell Phone, 292

total_phones = 458+437+141+924+292
prop_bb = 141 / total_phones
print(total_phones, prop_bb)

# 3 single proportion hypothesis test: Hnull == 0.05, Halt >= 0.05, right tail
runner([0.0033, 0.0042, 0.0044, 0.0041, 0.0043], 3)  # by prop
runner([0.004, 0.0033, 0.0051, 0.0045, 0.0046], 3)  # by count

# 4 95%CI for pop median from BodyTemp50: CI for single param
runner([98.45-98.0, 98.45-98.0, 98.45-98.0], 4)

# 5 90%CI for pop mean from manhattan apartments
runner([3693.775-2713.625, 3688.750-2713.425, 3693.125-2714.025], 5)

# 6 difference in means hypothesis test: Ho: mu1 == mu2, Ha: mu1 != mu2, 2 tail
runner([0.0037*2, 0.0024*2, 0.0019*2, 0.0017*2, 0.003*2], 6)

# %%
