customer = {          # This is dictonary...'{}' bracket is for dictonary...these are mutable
     "name": "Pulkit",
     "age": 21,
     "gender": "Male",
     "birthYear": 2001,
     "birthPlace": "Chandigarh"
}

print(customer["name"])
print(customer["birthYear"])




# Digits to Letters
phone = input("Phone Number (IN): ")
digits = {   # Created a dictonary cz in dictonary we can assign a 'KEYWORD' to a 'VALUE'
     "1": "One",
     "2": "Two",
     "3": "Three",
     "4": "Four",
     "5": "Five",
     "6": "Six",
     "7": "Seven",
     "8": "Eight",
     "9": "Nine"
}

output=""
for i in phone:
     output += digits.get(i, "!!") + " "  # Here we used for loop to go thru the elements of var phone and then we used 'i' variable to call the keywords in our dictonary digits and we used .get() so that if user inputs something foreign then our code shouldnt yell and give '!!' as output for it and then we put that result in the ouput variable for print
print(output)