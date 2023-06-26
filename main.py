import random
print("Welcome to the Rock, Paper, Scissor Game \n")
computer_wins = 0
user_wins = 0
number_of_ties = 0

while True:
  #list of alternatives
  alternatives = "1: Scissor", "2: Rock", "3: Bag"
  
  #start of game
  print ("Your alternatives are the following:\n", alternatives)
  computer_choice = random.choice(alternatives)
  #contol user input to int
  while True:
    try:
      user_choice = int(input("What's your choice? \n Choose by writing the number representing the weapon of choice:"))
      break
    except:
      print("Please write a number between 1-3 to choose your weapon.")
      
  
  #computer wins outcomes
  if int(user_choice) == 1 and computer_choice == alternatives[1]:
    print ("The computer wins...")
    print ("The computers choice of rock beats your scissors")
    computer_wins += 1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  elif int(user_choice) == 3 and computer_choice == alternatives[0]:
    print ("The computer wins...")
    print ("The computers choice of scissors beats your bag")
    computer_wins += 1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  elif int(user_choice) == 2 and computer_choice == alternatives[2]:
    print ("The computer wins...")
    print ("The computers choice of bag beats your rock")
    computer_wins += 1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  
  #user wins outcomes
  elif int(user_choice) == 1 and computer_choice == alternatives[2]:
    print ("You win!")
    print ("The computers choice of bag loses your scissors")
    user_wins += 1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  elif int(user_choice) == 2 and computer_choice == alternatives[0]:
    print ("You win!")
    print ("The computers choice of scissors loses to your rock")
    user_wins += 1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  elif int(user_choice) == 3 and computer_choice == alternatives[1]:
    print ("You win!")
    print ("The computers choice of rock loses to your bag")
    user_wins += 1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  
  #Ties
  
  elif int(user_choice) == 1 and computer_choice == alternatives[0]:
    print ("It's a tie...")
    print ("The computers choice of scissors ties your scissors")
    number_of_ties +=1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  elif int(user_choice) == 2 and computer_choice == alternatives[1]:
    print ("It's a tie...")
    print ("The computers choice of rock ties your rock")
    number_of_ties +=1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  elif int(user_choice) == 3 and computer_choice == alternatives[2]:
    print ("It's a tie...")
    print ("The computers choice of bag ties your bag")
    number_of_ties +=1
    print("Computer Wins:", int(computer_wins), "User Wins:", int(user_wins), "Number of Ties: ", int(number_of_ties))
    input("Press Enter to Play Again")
  else:
    print("Try something else")








