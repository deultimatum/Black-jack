import random
from image import black_jack_logo
from replit import clear

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def deal_card():
  """Returns random random cards from a deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_score(cards):
  """Checks and returns the sum of cards is 21 or not."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0 
  
  if 11 in card sum(cards) > 21:
    
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  
  
  
  

user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
  user_card.append(deal_card())
  computer_card.append(deal_card())
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"user cards are {user_cards} and current score : {user_score}")
    print(f'computer card are {computer_cards[0]} ')
  
  
