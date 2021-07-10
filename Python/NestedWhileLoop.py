# For star like shape for string

name='CHITKARA'
for i in range(len(name)): #Rows     It was 1 , len(name) which made it print C and H together but we cant it to start from index 0

     for j in range(i + 1): #Columns
          print(name[j],end = " ") 
     print()

print('\n');




# For single character in a row

for i in (name):
     print(i)

print('\n')



# 3rd value is the increment value in for loop 

for i in range(1,51,3):
     print(i,end = " ")

print('\n')



# While loop for star like shape for numbers

i=1
while i<=5:
     j=1
     while j<=i:
          print(j,end= " ")
          j+=1
     i+=1
     print()

print('\n')




# For loop for the star like shape of numbers

for i in range(1, 6):
     for j in range(1, i + 1):
          print(j,end= " ")
     print()

print('\n')