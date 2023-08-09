alphabet_clair = 'abcdefghijklmnopqrstuvwxyz'
alphabet_code = 'bcdefghijklmnopqrstuvwxyza'
message_clair = 'gymnase de beaulieu'
message_code = ''
for c in message_clair:
    if c == ' ':
        message_code = message_code+c
    else:
        index = alphabet_clair.index(c)
        message_code = message_code + alphabet_code[index]
print(message_clair)
print(message_code)