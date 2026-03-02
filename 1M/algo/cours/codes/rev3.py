n = int(input("Entrez un nombre entier décimal : "))
bits = []

if n == 0:
    bits = [0]
else:
    while n > 0:
        if n % 2 == 0:
            bits.append(0)
        else:
            bits.append(1)
        n = int(n/2)


binary = ""
i = len(bits) - 1
while i >= 0:
    binary += str(bits[i])
    i  = i - 1

print("Représentation binaire :",binary)