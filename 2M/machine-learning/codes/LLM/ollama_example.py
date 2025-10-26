import ollama

question = input("Salut, comment puis-je t'aider aujourd'hui : ")

response = ollama.chat(model='phi4-mini', messages=[
#  {'role': 'user', 'content': 'Ecris-moi un code Python pour résoudre une équation du 2ème degré sans fonction ni module externe'}])
  {'role': 'user', 'content': question}])

print(response['message']['content'])