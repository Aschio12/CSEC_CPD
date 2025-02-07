words=input()
uppercase=0
lowercase=0
for letter in words:
    if letter==letter.upper():
        uppercase+=1
    else:
        lowercase+=1
if uppercase>lowercase:
    print(words.upper())
else:
    print(words.lower())
