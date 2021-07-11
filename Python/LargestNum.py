list = [1,2,4,5,6,7,8,1,2,100,45552,22,19902213445642223]
largest = list[0]  # Here we suppose that the index 0 element is the largest num
for i in (list):  # This line makes i iterate thru all the list
     if i > largest:
          largest = i
print(f"Largest Number in the list is: {i}") 