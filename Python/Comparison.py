name = input("What is your name ")
if len(name) < 3: # Greater than op
     print("Name must be atleast 3 characters long")
elif len(name) > 50: # Less than op 
     print("Name can be maximum of 50 characters")
else:
     print("Name looks good !!")