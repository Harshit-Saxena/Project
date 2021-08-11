# For star like shape for string

name='CHITKARA'
for i in range(len(name)): #Rows     It was 1 , len(name) which made it print C and H together but we cant it to start from index 0
     for j in range(i+1): #Columns  Range by default is from index 0
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

for i in range(1,6):
     for j in range(1, i + 1): # If we wrote 1,i then it will be 1,5 which means it will go to 4 only but we want 5 as well so we hv to write i + 1
          print(j,end= " ")
     print()

print('\n')






# Making F shape with nested loops

numbers = [5,2,5,2,2]
for x_count in numbers:
     output = ''
     for count in range(x_count):
          output +='x'
     print(output)
print('\n')







# Making L shape with nested loops

numbers = [2,2,2,2,5]
for x_count in numbers:
     output=''
     for count in range(x_count):
          output+='x'
     print(output)