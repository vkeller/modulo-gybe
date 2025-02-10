u = 0.6
for i in range(100):
    u0 = 2*u
    if u0 > 1:
        u0 = u0 - 1
    print(u0)
    u = u0