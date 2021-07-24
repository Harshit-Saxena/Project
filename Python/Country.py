
#  TODO: User input of 8 countries
#  TODO: Display them in  Sr.No  Country  Length Of Name
#  TODO: Find the country with max alphabets
#  TODO: Sort them in alphabetical order

countries = []

# * Inputting countries

for num in range(8):
     country = input(f"Enter country { num+1 } name: ").capitalize()
     countries.append(country)
print()



# * Display in order

print(f"Sr.No\tCountry\t\tLength of Name")
print()
for num in range(8):
     print(f"{num+1}\t{countries[num]}\t\t{len(countries[num])}")
print()



# * Find max_len country

max_len = 0
for name in countries: 
    if(len(name) > max_len): 
        max_len = len(name)
        longest_name = name
print(f"The country with the maximum character is: {longest_name}")
print()



# * Sorting countries

countries.sort()
# print(countries)  This will print it in form of list

print(f"Countries in an alphabetical order")
for name in countries: # * This will print each name seprately 
     print(name,end = ' ')