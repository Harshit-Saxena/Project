num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))

print()

print("Arithematic operation choices")
print(f"1: For addition")
print(f"2: For subtraction")
print(f"3: For multiplication")
print(f"4: For division")
print(f"5: For modulus")
choice = int(input("Enter your choice"))
if choice == 1:
     result = num1+num2
     print(f"Result of addition is: {result}")
elif choice == 2:
     result = num1-num2
     print(f"Result of subtraction is: {result}")
elif choice == 3:
     result = num1*num2
     print(f"Result of multiplication is: {result}")
elif choice == 4:
     result = num1/num2
     print(f"Result of division is: {result}")
elif choice == 5:
     result = num1%num2
     print(f"Result of modulus is: {result}")
else:
     print(f"{choice} is invalid choice")