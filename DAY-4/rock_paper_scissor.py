rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

asciisss = [rock,paper,scissors]

vs_art = r"""
\   /  ___ 
 \ /  /__  
  V   ___/ 
"""



logo = fr''' 
  _____            _           _____                             _____      _                    
 |  __ \          | |         |  __ \                           / ____|    (_)                   
 | |__) |___   ___| | ________| |__) |_ _ _ __   ___ _ __ _____| (___   ___ _ ___ ___  ___  _ __ 
 |  _  // _ \ / __| |/ /______|  ___/ _` | '_ \ / _ \ '__|______\___ \ / __| / __/ __|/ _ \| '__|
 | | \ \ (_) | (__|   <       | |  | (_| | |_) |  __/ |         ____) | (__| \__ \__ \ (_) | |   
 |_|  \_\___/ \___|_|\_\      |_|   \__,_| .__/ \___|_|        |_____/ \___|_|___/___/\___/|_|   
                                         | |                                                     
                                         |_|                                                     
'''


import random as rn
print(logo)
asciii = [rock,paper,scissors]
user_input = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissor"))-1
computer_input = rn.randint(0,2)


print(f"Your Choise:\n{asciisss[user_input]}")
print(vs_art)
print(f"\nComputer's Choise:\n{asciisss[computer_input]}")

if user_input==computer_input:
    print("IT's A TIE.")

elif (user_input==0 and computer_input==2) or (user_input==2 and computer_input==1) or (user_input==1 and computer_input==0):
    print("YOU WIN!!")

elif (computer_input==0 and user_input==2) or (computer_input==2 and user_input==1) or (computer_input==1 and user_input==0):
    print("YOU LOST, try again")