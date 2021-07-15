def emoji_converter(message):
     words = message.split(" ")
     emoji = {
          ";)": "😄",
          ";(": "😔"
     }
     output = ""
     for i in words:
          output += emoji.get(i, i) + " "
     return output
message = input(">: ")
print(emoji_converter(message))