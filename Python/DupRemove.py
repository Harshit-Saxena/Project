#Removing dups from the list 

list = [2,2,1,3,5,7,5,1,6,9,1]
uniques=[]
for number in list:  # This line is to make the number variable go thru all elements of the list
     if number not in uniques:
          uniques.append(number)
uniques.sort()
print(uniques)
print()