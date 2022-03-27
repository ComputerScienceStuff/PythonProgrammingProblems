words = []
  
with open('Input-03.txt', 'r') as myfile:
  for word in myfile:
    words.append(word)


with open("03-Snider.txt", 'w') as f:
  for w in words:
    #sum is a built in python thing for adding two numbres. so sum is basically: add int(number) in the line for each number in the line and get rid of the comma in between.
    ans = sum([int(i) for i in w.split(',')])
    #reuse code from last problem and compare them
    if ans > 5:
      f.write("1 \n")
    else:
      f.write("0 \n")

