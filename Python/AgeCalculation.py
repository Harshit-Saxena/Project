birth_yr = input("Birth year : ")

# age = 2021 - birh_yr error cz str is getting subtracted from integer

age = 2021 - int(birth_yr) # * Here we convert str birth_yr to integer for the calculation to work

result = str(age) # *I came up with this on my own 🤩...age is an integer aftr the calculation and we CANNOT concatenate integer to a string so I had to convert age into str for it to work 

# int() converts str to int 
# float() converts str to float 
# bool() converts str to bool 
#str() converts variable to str

print("You are " + result + " years old")