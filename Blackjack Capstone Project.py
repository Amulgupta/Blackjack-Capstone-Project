import random
from art import logo

def deal_card():
  """This function will pick up a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """This will calculate the sum of cards of the user or the dealer."""
  if sum(cards) == 21 and len(cards) == 2:   #Check for Blackjack.
    return 0

  if 11 in cards and sum(cards) > 21:     #Check for ace and if sum exceeds 11 take ace as 1.
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score :
    return "Draw 😶"

  elif computer_score == 0:
    return "Lose, Dealer has a Blackjack 😭"

  elif user_score == 0:
    return "Win with a Blackjack 😂"

  elif user_score > 21:
    return "You went over, you lose 😪"

  elif computer_score > 21 :
    return "You won. Opponent went over 😎"

  elif user_score > computer_score:
    return "You win 😃"

  else:
    return "You lose 😫"

def play_game():
  
  print(logo)
  
  user_cards  = []
  computer_cards = []
  
  is_game_over = False
  for _ in range(2):           #Drawing a card.
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  
  while not is_game_over :
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    
    else:
      reply = input("Do you want to draw another card ?y/n ").lower()
      if reply == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17 :
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"    Your final hand: {user_cards}, final score: {user_score}")
  print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  play_game()
