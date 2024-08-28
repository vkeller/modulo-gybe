x = 2.
b_inf = 1.
b_sup = x
m = 0.
m_carre = 0.
for i in range(100):
    m = (b_inf + b_sup)/2
    m_carre = m**2
    if m_carre > x :
        b_sup = m
        b_inf = b_inf
    else:
        b_sup = b_sup
        b_inf = m
print("Racine de ",x," = ",m)