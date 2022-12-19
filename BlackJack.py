import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare_score(user_score, computer_score):
  if user_score == computer_score:
    return "DRAW"
  elif computer_score==0:
    return "You Lose opponent has BlackJack"
  elif user_score==0:
    return "You Win you have BlackJack"
  elif user_score>21:
    return "you went over, You Lose"
  elif computer_score>21:
    return "opponent went over, You win"
  elif user_score> computer_score:
    return " You Win"
  elif computer_score> user_score:
    return " You Lose"

User_cards = []
computer_cards = []
is_game_over= False
for i in range(2):
  User_cards.append(deal_card())
  computer_cards.append(deal_card())
while not is_game_over:
  user_score=calculate_score(User_cards)
  computer_score=calculate_score(computer_cards)
  print(f"Your cards :{User_cards}, current score:{user_score} ")
  print(f"Computers first card :{computer_cards[0]}")
  if user_score==0 or computer_score==0 or user_score>21:
    is_game_over= True
  else:
    X=input("type 'Y' to get another Card or 'N' to pass : ").lower()
    if X=='y':
      User_cards.append(deal_card())
    else:
      is_game_over=True
while computer_score !=0 and computer_score<17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
print("-----------------------------------------------------------")
print(f"Your final hand:{User_cards} and final score :{user_score}")
print(f"computer final hand:{computer_cards} and final score :{computer_score}")
print(compare_score(user_score , computer_score))