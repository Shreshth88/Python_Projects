import random
print("Welcome To Toss the Coin\n")
print('You have two option i.e. either "Head" or "Tail"\n')
random_toss=random.randint(0,1)
if random_toss == 0:
    print("It's Head\n")
else:
    print("It's Tail")