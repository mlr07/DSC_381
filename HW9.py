import pandas as pd
from statistics import mean


# # 1
# data = "./data/SalaryGender.csv"
# df = pd.read_csv(data)
# # h_null = 50
# # h_alt <= 50
# print(df.columns)
# print(df["Age"].mean())
# runs = round(mean([0.021, 0.021, 0.020, 0.019, 0.021, 0.021]), 4)
# print(runs)


# # 2
# # curl -o StudentSurvey.csv https://www.lock5stat.com/datasets3e/StudentSurvey.csv
# data = "./data/StudentSurvey.csv"
# df = pd.read_csv(data)
# df["MathSAT"].to_csv("./data/MathSAT.csv", index=False)
# runs = round(mean([615.326-603.58, 615.334-603.526, 615.251-603.503, 615.282-603.450]))
# print(runs)

# # 3
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

runs = round(mean([0.110, 0.111, 0.112, 0.108]),3)
print(runs)

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

runs = round(mean([0.360, 0.367, 0.361, 0.360, 0.362]),3)
print(runs)


