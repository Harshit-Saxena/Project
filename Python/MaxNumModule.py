# Max num in list
def find_max(numbers):
     largest = numbers[0]
     for i in numbers:
          if i > largest:
               largest = i
     return(f"Largest number in the list is: {i}")



# Min num in list
def find_min(numbers):
     smallest = numbers[0]
     for x in numbers:
          if x < smallest:
               smallest = x
     return(f"Smallest number in the list is: {x}")