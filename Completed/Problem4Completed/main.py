words = []

#slice the first letter of the string. -> keep the string saved
def capitalize(s:str) -> str:
  #uppercase the first letter of the word then join the rest of the letters
  return s[0].upper() + s[1:]
  
with open('Input-04.txt', 'r') as myfile:
  for word in myfile:
    words.append(word)


with open("04-snider.txt", 'w') as f:
  for w in words:
    f.write(capitalize(w))
    

