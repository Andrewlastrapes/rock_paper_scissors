# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)


def rock_paper_scissors():
  Player1 = input("Player 1, Please enter rock, paper or scissors: ")
  print()
  Player2 = input("Player 2, Please enter rock, paper or scissors: ")
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
  elif(Player1 != "rock", Player1 != "paper", Player1 != "scissors", Player2 != "rock", Player2 != "paper", Player2 != "scissors"):
    print()
    print("Invalid entry")
  else: 
    print()
    print("Tie")

rock_paper_scissors()