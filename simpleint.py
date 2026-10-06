def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si


# Fixed values — no user input
p = 10000
r = 5
t = 2

result = simple_interest(p, r, t)

print("Principal:", p)
print("Rate:", r, "%")
print("Time:", t, "years")
print("Simple Interest:", result)