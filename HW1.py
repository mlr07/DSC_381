def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def perm_no_rep(n, r):
    return (factorial(n) / (factorial(n - r)))


def per_with_rep(n, r):
    return n ** r


def combo_no_rep(n, r):
    return (factorial(n) / (factorial(r) * factorial(n-r)))


def combo_with_rep(n, r):
    return (factorial(n + r - 1) / (factorial(r) * factorial(n - 1)))


# Deck
# deck = 52
# rank = 13
# suit = 4

# 1A
# PrA = 1 - ((48/52)*(47/51))
# print(f"Pra: {PrA}")


# 1B
# PrB = 1 - ((48/52)*(47/51)*(46/50)*(45/49)*(44/48))
# print(f"PrB: {PrB}")


# 1C
# PrC = 3/(deck-1)
# print(f"PrC: {PrC}")


# 1D
# diamond5 = combo_no_rep(13, 5)
# print(f"diamond 5 combo: {diamond5}")

# deck5 = combo_no_rep(52, 5)
# print(f"deck 5 combo: {deck5}")

# PrD = diamond5 / deck5
# print(f"PrD 5 diamonds: {PrD}")


# 1E
# kind3 = combo_no_rep(13, 1) * combo_no_rep(4, 3)
# print(f"kind3: {kind3}")

# kind2 = combo_no_rep(12, 1) * combo_no_rep(4, 2)
# print(f"kind2: {kind2}")

# PrE = (kind3 * kind2) / combo_no_rep(deck, 5)
# print(f"PrE full house: {PrE}")

print("-"*20)

# X = combo_no_rep(5, 2)
# print(X)

Nac = factorial(52) / factorial(52-10)
N = 52**10
Pr_A = Nac / N

print(Nac)
print(N)
print(Pr_A)