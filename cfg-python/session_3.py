# #3.1
# price = float(input("What is the price of a burger? "))
# within_budget = price <= 10.0
#
# print("Burger is within budget: {}".format(within_budget))

#3.2
# price = float(input("What is the price of a burger? "))
# veggie_option= input("Is there a vegetarian option? y/n: ")
#
# within_budget = price <= 10.0
# has_veggie= veggie_option=="y"
#
# criteria_met = within_budget and has_veggie
#
#
# print("Restaurant meets criteria: {}".format(criteria_met))

#3.3
# price = float(input("What is the price of a burger? "))
# veggie_option= input("Is there a vegetarian option? y/n: ")
#
# within_budget = price <= 10.0
# has_veggie= veggie_option=="y"
#
# criteria_met = within_budget and has_veggie
#
# if criteria_met:
#     print("This restaurant is a good choice!")
# if not within_budget or not has_veggie:
#     print("Probably not a good idea")

#3.3
#
# meal_price=float(input("how much did the meal cost? "))
#
# discount_choice=input("do you have a discount? y/n ")
# discount_applicable= discount_choice=="y" and meal_price>20.0
#
# if discount_applicable:
#     print("discount applied")
#
# else:
#     print("no discount")

#3.5
#temp = float(input("What is the oven temperature? "))
#
# if temp > 200:
#     print("oven is too hot")
# elif temp < 150:
#     print("oven is too cold")
# elif temp == 180:
#     print("oven is at the perfect temperature")
# else:
#     print("temperature is close enough")

#3.6
# import random
#
# def flip_coin():
#     random_number = random.randint(1, 2)
#     if random_number == 1:
#         side = 'heads'
#     else:
#         side = 'tails'
#     return side
#
# choice = input('heads or tails: ')
# if choice != "heads" and choice !="tails":
#     print("you can only choose heads or tails")
#
# else:
#     result = flip_coin()
#     print('The coin landed on {}'.format(result))
#
#     if result == choice:
#         print("you win!")
#     else:
#         print("you lose :(")

import random
def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice
my_choice = input('Choose rock, scissors or paper: ')

if choice != "rock" and choice !="scissors" and choice !="paper":
    print("you can only choose rock, scissors or paper")

opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')

if my_choice == 'scissors' and opponent_choice == 'paper':
    print('You win!')

if my_choice == 'paper' and opponent_choice == 'rock':
    print('You win!')