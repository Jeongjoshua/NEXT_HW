print("what is the maximum number?")
maxNum = int(input())
max = maxNum
min = 0
test = int(maxNum/2)
counter = 1


while True:
  print("Is your answer "+ str(test)+ " answer in higher, lower, correct")
  reply = str(input())
  if reply == "higher":
        min = test
        counter+=1
        test = int((max+min)/2)
        continue
    
  if reply == "lower":
        max = test
        counter+=1
        test = int((max+min)/2)
        continue
  else: 
    print("took " + str(counter) + " tries")
    break