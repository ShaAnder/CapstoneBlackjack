#!usr/bin/env/python

### --- IMPORTS --- ###

#we want random to randomize the draw
import random
#import time to deal with sleeping
import time
#import our logo for flair
from art import logo
#import for our clear func
from os import name, system

### --- VARIABLES --- ###

#as we don't have a way to differenciate (yet) the face cards and the ace, we set all face cards to 10 and ace to 11 (ace can be 1 or 11)
#this will be useful later when we are deciding winners
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#we create a hand for the user and computer
user_hand = []
computer_hand = []

### --- FUNCTIONS --- ###

#clear func for console
def clear():
    """clears the console
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#we create a draw function for both user and computer (singular for both to prevent repeats)
def draw(x):
  """draws cards
  """
  #empty card list
  card = []
  #for loop, for card in range of amount we choose to draw
  for c in range(0, x):
    #append the cards to the list for that player
    card.append(random.choice(cards))
  #return the list  
  return card

#we create a reset for playing again, this just clears the cards in the hands and resets the console
def reset():
    """resets the game
    """
    #global cards
    global cards
    global user_hand
    global computer_hand
    #our clear func
    time.sleep(3)
    clear()
    #defauls
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    computer_hand = []

#calculates the score
def calculate_score(x):
  """calculates the score, accounts for aces drawn
  """
  #score is the sum of x our number of cards
  score = sum(x)
  #if a player drew an 11 (ace) and the score is over 21, this will set the ace to 1 
  if 11 in x and score >21:
    #instead of searching for 11 in the index, searches for instances of 11 if it finds one sets to 1
    x[x.index(11)] = 1 
  #tallies and returns the score
  score = sum(x)
  return score

#main function
def main():
  """main program function typed once to prevent repitition
  """
  #prints our welcome
  print(logo)
  print("Welcome to the table")
  #extends the user and cpu lists with draw function of 2 cards (extend instead of append)
  #we use this as we are adding a list to a list effectively (the draw returns a list)
  user_hand.extend(draw(2))
  computer_hand.extend(draw(2))
  #calculates each players score
  user_score = calculate_score(user_hand)
  computer_score = calculate_score(computer_hand)  
  #prints the cards drawn for each player
  print(f"Cards drawn. Player Cards: {user_hand}. Dealer Cards: {computer_hand[0]}, ?")
  #shows us user only score
  print(f"Player Score: {user_score}")
  #do we want to draw more cards
  Another = True
  #while another card = true
  while Another == True:
    #ask the user if they want to draw
    more = input("Would you like to draw another card? Y or N: ").lower()
    #if y
    if more == 'y':
      #extend another card, recalc score and display current score/ cards
      user_hand.extend(draw(1))
      user_score = calculate_score(user_hand)
      print(f"Player has drawn another card. Current cards: {user_hand}, Current score: {user_score}")
      #if score is over 21 (and this also accounts for aces)
      if user_score > 21: 
        Another = False
    #if more = n kill loop
    if more == 'n':
      Another = False
  #we want the cpu to reveal at 16 or more score (as is often the rule in blackjack (dealer draws till 16 or higher))
  #if score is more than 16 reveal
  if computer_score >= 16: 
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
  #else
  else:
    #while it's less than 16
    while computer_score < 16:
      #draw until it hits 16 or more
      computer_hand.extend(draw(1))
      computer_score = calculate_score(computer_hand)
      #if computer score is over 21, computer bust, user wins
      if computer_score > 21:
      #kill loop
        Another = False
  #finally win conditions
  clear()
  print(logo)
  if computer_score > 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("House Bust, Player Wins!")
  if user_score > 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("Player Bust, House Wins")
  elif user_score == 21 and computer_score == 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("A double blackjack, however house always wins...")
  elif user_score == 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("Blackjack! Player Wins")
  elif computer_score == 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("Blackjack! House Wins")
  elif user_score > computer_score and user_score < 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("Player Wins")
  elif computer_score > user_score and computer_score < 21:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("House Wins")
  else:
    print(f"Players cards: {user_hand}, Players score: {user_score}")
    print(f"Dealers Cards: {computer_hand} Dealers Score: {computer_score}")
    print("House Wins")

### --- EXECUTION --- ###

#we have it run the main function
main()
#ask for another game
another_game = input("Play Again? Y or N:").lower()
play_again = True
#if they wanna play again
while play_again == True:
  if another_game == 'y':
    reset()
    main()
    another_game = input("Play Again? Y or N:").lower()
  #if not end loop clear it all up
  elif another_game == 'n':
    play_again = False
    print("Goodbye")
    time.sleep(3)
    clear()
    

