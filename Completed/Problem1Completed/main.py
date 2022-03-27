words = []


  
with open('Input-01.txt', 'r') as myfile:
  for word in myfile:
    words.append(word)


with open("01-Snider.txt", 'w') as f:
  for w in words:
    x = 0
    amount = int(words[0])
    while x < amount:
      f.write("hello \n")
      x += 1
    

