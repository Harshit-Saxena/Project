import random
# to get 2 random num btw 0 and 1
for i in range(2):
     print(random.random())
print()


# to get 2 random num btw 10 and 20
for i in range(2):
     print(random.randint(10,20))
print()


# to get a random choice from the list
food = ['Corns','Ice cream','Pasta','Noodles','Spring Roll']
order = random.choice(food)
print(order)
print()