

def syr(n):
	if (n % 2 == 0):
		return n / 2
	else:
		return 3 * n + 1

N = 0

try:
	N = int(input('Entrez un chiffre : '))
	print("Vous avez entré ",N)
	while (N !=1) :
		N = syr(N)
		print(N)    
except EOFError as e:
    print(e)




