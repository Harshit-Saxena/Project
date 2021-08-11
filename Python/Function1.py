def greeting(first_name,last_name):
     print(f"Hello {first_name} {last_name}")
     print(f"Welcome to our program.")
     print(f"Here {first_name} used the function in python for first time")
     print()

greeting("Pulkit","Saxena")   # first_name and last_name are positional arguments cz their position matters and needs to be same as above

greeting(last_name="Saxena",first_name="Pulkit") # these are keyword arugments and in these the order doesnt matter but we should prefer to use positional BUT when hving numeric value as arguments we must use keyword to improve quality of code

# ! keyword argument should ALWAYS come after the positional argument otherwise python will give error 