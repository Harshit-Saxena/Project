secret_num = 5
guess_count = 0
guess_limit = 3
k =""

while guess_count < guess_limit:
     guess = int(input("Guess: "))
     guess_count+=1
     if guess == secret_num:
          print("You Won")
          break
else:
     print("Sorry you ran out of chances")
     print('\n')
     print(f"{secret_num} was the secret number")

k=input("Press enter to exit !! ")