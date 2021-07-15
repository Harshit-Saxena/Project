try:
     age = int(input("Age: "))
     income = 20000
     risk = income // age     # '/' given decimal or float value and '//' gives integer value
     print(risk)
except ValueError:
     print("Invalid Value")
except ZeroDivisionError:
     print(f"Age cannot be 0")
     print(f"Please enter a valid age")