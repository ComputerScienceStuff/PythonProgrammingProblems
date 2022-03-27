words = []

with open('Input-05.txt', 'r') as myfile:
  for word in myfile:
    words.append(word)


with open("05-Snider.txt", 'w') as f:
  for w in words:
    w[-1].upper()
    test = w[0:-2] + w[-1]
    f.write(test)
    
#it slices the last letter but doesn't rejoin it
