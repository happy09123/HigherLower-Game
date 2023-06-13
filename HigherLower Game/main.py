import game_data
import random
from replit import clear
# import os
# def clear_console():
#   os.system('clear')

A = game_data.data[random.randint(0, len(game_data.data)-1)]
B = game_data.data[random.randint(0, len(game_data.data)-1)]

score = 0
finished = False

while not finished:
  print(f"A: {A['name']}, a {A['description']}, from {A['country']}\nVs.\nB: {B['name']}, a {B['description']}, from {B['country']}")
  print(f"{A['name']}'s follower count is {A['follower_count']}\n{B['name']}'s follower count is {B['follower_count']}")
  question = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  clear() # clear_console()
  if (A['follower_count'] > B['follower_count']):
    if (question == "A"):
      score += 1
      print(f"You're right! Current score: {score}.")
    elif (question == "B"):
      print(f"You're wrong.\nFinal Score: {score}.")
      break
  elif (A['follower_count'] < B['follower_count']):
    if (question == "B"):
      score += 1
      print(f"You're right! Current score: {score}.")
    elif (question == "A"):
      print(f"You're wrong.\nFinal Score: {score}.")
      break
  A = B
  B = game_data.data[random.randint(0, len(game_data.data)-1)]
