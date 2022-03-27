words = []
  
with open('Input-02.txt', 'r') as myfile:
  for word in myfile:
    words.append(word)


with open("02-Snider.txt", 'w') as f:
  for w in words:
    if int(w) > 5:
      f.write("1 \n")
    else:
      f.write("0 \n")
