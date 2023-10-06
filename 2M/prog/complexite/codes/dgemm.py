# Multiplication matricielle
# Vincent Keller, 2023

m = 10
n = 8
A = [[0] * m] * m
B = [[0] * m] * n
C = [[0] * n] * m
for i in range(m):
    for j in range(n):
        for k in range(m):
            C[i][j] = A[i][k] * B[k][j]

print(A)
