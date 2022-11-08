try:
	print("Entrez un chiffre")
	i = input()
	a = int(i)
	print(a)
except EOFError as e:
	print(e)
