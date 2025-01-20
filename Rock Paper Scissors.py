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
import sys
import random
user_choice = int(input("Welcome to rock/paper/scissors.\nFor rock type 0, for paper type 1, for scissors type 2.\n"))

if not 0 <= user_choice <= 2:
    print("PLEASE TYPE 1, 2 OR 3!!!")
    exit()

list_words = ["rock", "paper", "scissors"]
list_rps = [rock, paper, scissors]
print(f"You have choosen {list_words[user_choice]}.")
print(list_rps[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer has choosen {list_words[computer_choice]}.")
print(list_rps[computer_choice])

if computer_choice == 0:
    if user_choice == 1:
        print("You have won.")
    elif user_choice == 0:
        print("It's a draw.")
    else:
        print("You have lost.")

if computer_choice == 1:
    if user_choice == 2:
        print("You have won.")
    elif user_choice == 1:
        print("It's a draw.")
    else:
        print("You have lost.")

if computer_choice == 2:
    if user_choice == 0:
        print("You have won.")
    elif user_choice == 2:
        print("It's a draw.")
    else:
        print("You have lost.")
input("Press enter to close program.")