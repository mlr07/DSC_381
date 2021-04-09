# %%
import pandas as pd
from statistics import mean
from IPython.display import Latex, display

# NOTE: clean up print and proporitons
# %%

def runner(runs:list=None, q:str=None) -> None:
    """
    Short function to track runs from Statkey.
    Args: 
        runs -> list of run results from statkey
        q -> string question number
    """

    if runs and len(runs) > 0:
        print(f"Q{q}: {len(runs)} run mean = {mean(runs):.3f}")
    else:
        print("No data")


# 1
data = "./data/SalaryGender.csv"
df = pd.read_csv(data)
# h_null = 50
# h_alt <= 50
print(df["Age"].mean())
runner([0.021, 0.021, 0.020, 0.019, 0.021, 0.021], "1")


# 2
# curl -o StudentSurvey.csv https://www.lock5stat.com/datasets3e/StudentSurvey.csv
data = "./data/StudentSurvey.csv"
df = pd.read_csv(data)
df["MathSAT"].to_csv("./data/MathSAT.csv", index=False)
runner([615.326-603.58, 615.334-603.526, 615.251-603.503, 615.282-603.450], "2")


# 3
# curl -o CocaineTreatment https://www.lock5stat.com/datasets3e/CocaineTreatment.csv
data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)

# relapse proportions
total = len(df["Relapse"])
relapse = round(sum(df["Relapse"] == "yes") / total, 3)
no_relapse = round(sum(df["Relapse"] == "no") / total, 3)
print(total, relapse, no_relapse)

# placebo proportions
total_placebo = df[df["Drug"]=="Placebo"]
placebo_no_relapse = round(sum(total_placebo["Relapse"] == "no") / len(total_placebo), 3)
print(placebo_no_relapse) 

# lithium proportions
total_lithium = df[df["Drug"]=="Lithium"]
lithium_no_relapse = round(sum(total_lithium["Relapse"] == "no") / len(total_lithium), 3)
print(lithium_no_relapse)

# desipramine proportions
total_desip = df[df["Drug"]=="Desipramine"]
desip_no_relapse = round(sum(total_desip["Relapse"] == "no") / len(total_desip), 3)
print(desip_no_relapse)


# 4
# H_null = 0.30
# H_alt =< 0.30
# p_hat = 0.30
data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)
placebo = df[df["Drug"]=="Placebo"]
sample = len(placebo)
count = sum(placebo["Relapse"] == "no")
p_no_relapse =  round(count / sample, 3)
print(sample, count, p_no_relapse)

runner([0.110, 0.111, 0.112, 0.108], "4")


# 5 
# H_null = h1 == h2
# H_alt = h1 =! h2
data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)
lithium = df[df["Drug"]=="Lithium"]
lithium_sample = len(lithium)
lithium_count = sum(lithium["Relapse"] == "no")
difference_p = (lithium_no_relapse - p_no_relapse)

print(f"lithium: count = {lithium_count}, sample size = {lithium_sample}")
print(f"placebo: count = {count}, sample size = {sample}")
print(f"lithium p = {lithium_no_relapse}, placebo p = {placebo_no_relapse}, difference = {difference_p}")

runner([0.360, 0.367, 0.361, 0.360, 0.362], "5")


# 6
# find 83% confidence in proportion difference
data = "./data/CocaineTreatment.csv"
df = pd.read_csv(data)

# desipramine no relapse
desip = df[df["Drug"]=="Desipramine"]
desip_sample = len(desip) 
desip_count = sum(desip["Relapse"] == "no")

# lithium no relapse
lithium = df[df["Drug"]=="Lithium"]
lithium_sample = len(lithium)
lithium_count = sum(lithium["Relapse"] == "no")

# print sample and count
print(f"desipramine: count = {desip_count}, sample size = {desip_sample}")
print(f"lithium: count = {lithium_count}, sample size = {lithium_sample}")

# track statkey runs
runner([0.500-0.167, 0.500-0.167, 0.500-0.167], "6")


# 7
# find 92% confidence for slope coeff between salary and age
data = "./data/SalaryGender.csv"
df = pd.read_csv(data)

# process data for input to statkey
df[["Salary", "Gender"]].to_csv("./data/Q7_SalaryGender.csv", index=False)

# track statkey runs
runner([0.403-0.097, 0.403-0.098, 0.403-0.099, 0.402-0.101, 0.406-0.099], "7")


# 8
# find 97% CI for SD of salaries
data = "./data/SalaryGender.csv"
df = pd.read_csv(data)

# process data for input to statkey
df[["Salary"]].to_csv("./data/Q8_SalaryGender.csv", index=False)

# track statkey runs
runner([49.011-34.349, 47.779-35.907, 49.124-34.446, 49.079-34.503, 49.032-34.369], "8")


# 9
# find 95% CI for median of ages
data = "./data/SalaryGender.csv"
df = pd.read_csv(data)

# process data for input to statkey
df[["Age"]].to_csv("./data/Q9_SalaryGender.csv", index=False)

# track statkey runs
runner([53.5-44.5, 53.5-44.5, 53.5-44.5], "9")

# %%
# 10
data = "./data/StudentSurvey.csv"
df = pd.read_csv(data).dropna()
df = df[["Weight", "SAT", "Pulse", "GPA", "BirthOrder", "Exercise"]]
df.to_csv("./data/Q10_StudentSurvey.csv", index=False)

print(df.describe())

# test stats
sat = "n = 357, r = 0.049, slope = +0.012, intercept = +142.28"
pulse = "n = 357, r = 0.0084, slope = +0.020, intercept = +158.47"
gpa = "n = 340, r = -0.192, slope = -14.929, intercept = +207.01"
birth = "n = 354, r = -0.056, slope = -1.892, intercept = +164.62"
exercise = "n = 356, r = 0.159, slope = +0.933, intercept = +152.23"

# p values
sat = [0.016, -0.042]
pulse = [-0.038, -0.600]
gpa = [-7.978, -25.966]
birth = [1.802, -3.545]
exercise = [1.296, 0.072]

# %%

# 11
# LaTeX for statement of hypothesis test
statement = Latex(r"$\Pr(p > 0.50 \mid H_{0} = True)$")
display(statement)

