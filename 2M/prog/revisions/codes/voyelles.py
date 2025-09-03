phrase = input("Entrez une phrase")
nbrvoyelles = 0
for i in range(len(phrase)):
    l = phrase[i] 
    if l == "a" or l == "e" or l == "o" or l == "i" or l == "u":
        nbrvoyelles+=1

print(phrase,"possède",nbrvoyelles,"voyelles")