
# Randomly generate a rock, paper or scissors choice to play against player 1

def rock_paper_scissors_comp(input):
  
  import random

  while True:
    print()
    Player1 = input("Player 1, Please enter rock, paper or scissors: ")
    print()
    Player2 = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chooses: " + Player2)
    if(Player1 == "rock" and Player2 == "scissors"):
      print()
      print("Player 1 wins")
    elif(Player1 == "paper" and Player2 == "rock"):
      print()
      print("Player 1 wins")
    elif(Player1 == "scissors" and Player2 == "paper"):
      print()
      print("Player 1 wins")
    elif(Player1 == "rock" and Player2 == "paper"):
      print()
      print("Player 2 wins")
    elif(Player1 == "paper" and Player2 == "scissors"):
      print()
      print("Player 2 wins")
    elif(Player1 == "scissors" and Player2 == "rock"):
      print()
      print("Player 2 wins")
    elif(Player1 == Player2):
      print()
      print("Tie")
    else:
      print("Invalid Entry")

rock_paper_scissors_comp(input)
