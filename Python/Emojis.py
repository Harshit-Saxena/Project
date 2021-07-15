k=""
message = input(">: ")
words = message.split(' ')
emoji = {     # Created a dictonary here
     ";)": "😄",
     ";(": "😔",
}

output=""
for i in words:
     output += emoji.get(i, i) + " "
print(output)

k=input("Press enter to exit !! ")