# HW3 Q7

p = 0.6
d = 90
r = 1.05

E_Xd = (r*p+(1/r*(1-p)))**d
print(f"E(Xd) = {E_Xd}")

E_Xd_sq = E_Xd**2
print(f"(E_Xd)**2 = {E_Xd_sq}")

E_sq_Xd = (r**2*p + ((1/r)**2*(1-p)))**d
print(f"E(Xd**2) = {E_sq_Xd}")

Var_Xd = E_sq_Xd - E_Xd_sq
print(f"Var(Xd) = {Var_Xd}")
