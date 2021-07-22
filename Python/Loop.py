i=1
while i <=10:  # ! ':' is very imp to go into the while loop 
     print(i, end = ' ') # Here we chngd the final value of \n which means nxt line but we chngd it to space
     i += 1

print() # * Here I added this to change the line after 1 loop is finished and then print 2nd loop in other  


i=10
while i>=1:
     print(i, end = ' ')
     i -= 1
print('\n')

# Shorter Way 

#for i in range(1, 12): 
#   print(i)



# Total of list items
prices = [10,20,30,40,50]
total = 0
for i in prices:
     total +=i
print(f"Total of the items in the list: Rs {total}")    
               

# While loop for verticle
list=[1,2,3,4,'Name','Place']
i=0
while i< len(list):
     print(list[i])
     i+=1