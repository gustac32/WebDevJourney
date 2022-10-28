# imports
import random
import time
# game vars
snake = ["🐍", 100]
money = ["💶", 50]
skull = ["💀", 3]
lemon = ["🍋", 1]
cherry = ["🍒", 20]
eball = ["🎱", 8]
seven = ["🧿", 7]
digits = [snake, money, skull, lemon, cherry, eball, seven]
cash = 50
print("Welcome to the slot machine!")
print("You have 50$, each spin costs 1$")
print("Good luck!")
print()

# functions


def odds(digits):
    choices = []
    for _ in range(random.randrange(3, 7)):
        choice = random.choices(digits)
        if choice not in choices:
            choices.append(choice)
    return choices


def spinner(digits):
    temp =
