import random

# total_nums = []

# for x in range(100):
#   current_num = random.randint(1, 100)
#   if current_num not in total_nums:
#     total_nums.append(random.randint(1, 100))

# print(total_nums)

# Rock beats scissors
# Scissors beats paper
# Paper beats Rock
# 
# CPU needs to randomly pick a state
# Player input to set player state
# Conditionals to check Player vs CPU

choices = ["Rock", "Paper", "Scissor"]

print("Welcome to Rock, Paper, Scissors. Prepare to play...")

cpu_choice = choices[random.randint(0, 2)]
player_choice = choices[int(input("Please choose: Rock[1], Paper[2], or Scissor[3] ")) - 1]

if cpu_choice == player_choice:
  print("It's a tie.")
elif cpu_choice == choices[0] &&