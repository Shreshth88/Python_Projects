import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options=[rock,paper,scissors]
user_choice=int(input("What do you wanna choice 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if 0<=user_choice<=2:
    print("Your Choice: \n")
    print(options[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer's Choice: \n")
    print(options[computer_choice])
    if user_choice == computer_choice:
        print("It's draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You Won")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Won")
    else:
        print("You Lose")
else:
    print("You have entered invalid input")