# ⭐⭐⭐ Simulate a deck of cards and draw 5 random cards
import random
cards = {
    "King": 'Diamond', 'spades', 'hearts', 'clubs',
    "Jack": 'Diamond', 'spades', 'hearts', 'clubs',
    "Queen": 'Diamond', 'spades', 'hearts', 'clubs',
    "10": 'Diamond', 'spades', 'hearts', 'clubs',
    "9": 'Diamond', 'spades', 'hearts', 'clubs',
    "8": 'Diamond', 'spades', 'hearts', 'clubs',
    "7": 'Diamond', 'spades', 'hearts', 'clubs',
    "6": 'Diamond', 'spades', 'hearts', 'clubs',
    "5": 'Diamond', 'spades', 'hearts', 'clubs',
    "4": 'Diamond', 'spades', 'hearts', 'clubs',
    "3": 'Diamond', 'spades', 'hearts', 'clubs',
    "2": 'Diamond', 'spades', 'hearts', 'clubs',
    "Ace": 'Diamond', 'spades', 'hearts', 'clubs'}
#it's not letting me take a pull request, help D:
print("we have a deck of cards. There is the normal cards. The 4 houses, Spades, Hearts, Diamonds, and clubs")
#
random_rank = random.choice(list(cards.keys()))
# cards == (cards.keys(cards_drawn))
random_suit = random.choice(cards[random_rank])
# while cards[cards_drawn] == 0:
print(f"You drew: {random_rank} of {random_suit}")

