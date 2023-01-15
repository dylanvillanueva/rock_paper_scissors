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

hand = [rock, paper, scissors]
computer_choice = random.randint(0, len(hand) - 1)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice > 2 or user_choice < 0:
    print("Invalid choice")
else:
    print(hand[user_choice])
    print(f"Computer chose:\n{hand[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice > computer_choice:
        if user_choice == 2 and computer_choice == 0:
            print("You lose")
        else:
            print("You win")
    elif computer_choice > user_choice:
        if computer_choice == 2 and user_choice == 0:
            print("You win")
        else:
            print("You lose")