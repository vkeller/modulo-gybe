limit = int(input("Limite : "))
num = 2

# Boucle 1 : Parcourir les nombres de 2 à la limite
while num <= limit:
    is_prime = True
    i = 2
    
    # Boucle 2 : Tester les diviseurs potentiels
    while i < num:
        # Test 1 : Vérifier la divisibilité
        if num % i == 0:
            is_prime = False
            break
        i += 1
    
    # Test 2 : Vérifier si le nombre est premier
    if is_prime:
        print(num, "est premier")
    
    num += 1