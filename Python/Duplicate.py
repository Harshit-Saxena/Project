list = ['Rajesh',1,2,3,'Rajesh',6,8,10,'Rajesh']
search = "Rajesh"
for i in range(len(list)):
     if list[i] == search:
          print(f"Index of {search} in list is: {i}")