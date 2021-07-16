name = input(f"Enter your name: ")
total = 0
for i in name:
     if(i=='a' or i=='e' or i=="i" or i=="o" or i=="u"):
          total +=1
print(f"Number of vowels in string: {total}")