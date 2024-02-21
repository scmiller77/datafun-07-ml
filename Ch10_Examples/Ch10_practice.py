# Chapter 10 Practice

from account import Account 
from decimal import Decimal

from timewithproperties import Time

from deck import DeckOfCards
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# Practice from 10.2 and 10.3, using Account class 
account1 = Account('Stephen Miller', Decimal('12.24')) #Stephen makes an account

account1.deposit(Decimal('99.10')) #Stephen is paid for flippin burgers

account1.withdraw(Decimal('14.43')) #Stephen can't resist said burgers

print(account1.balance)

#account1.withdraw(Decimal('350.14')) #Stephen can't escape from student loan payments

#10.4 and 10.5
wake_up = Time(hour=6, minute=30)  #Dear lord noooooo

print(wake_up)

wake_up.hour = 7  #Late start Friday, Woop Woop

print(wake_up)

#10.6
deck_of_cards = DeckOfCards()

#print(deck_of_cards)

print(deck_of_cards.deal_card())

