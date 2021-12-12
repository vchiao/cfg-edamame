# #4.1
# clothes = [
#     "shorts",
#     "shoes",
#     "t-shirt",
# ]
#
# if clothes[0]=="shorts":
#     clothes[0]="warm coat"
#
# print(max(clothes))


# 4.2
# scores=[3,200,100,40,30,50,70,80,90,100]
#
# print("Number of scores: {}".format(len(scores)))
# print("Lowest score: {}".format(min(scores)))
# print("Highest score: {}".format(max(scores)))
#
# print(list(reversed(sorted(scores))))

# 4.3
# shopping_list=[
#   "bread",
#   "milk",
#   "eggs"
#   ]
#
# if "bread" in shopping_list:
#     shopping_list.append("butter")
#
# print(shopping_list)

# 4.4
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0
#
# for daily_cost in costs:
#     total_cost=total_cost+daily_cost
#
# print(total_cost)

# 4.5
# place = {
#     'name': 'The Anchor',
#     'post_code': 'E14 6HY',
#     'street_number': '54',
#     'location': {
#         'longitude': 127,
#         'latitude': 63,
#     }
# }
#
# print(place['post_code'])
# print(place['street_number'])
#
# print(place['latitude'])

4.6
fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]


for fruit in fruits:
    print(fruit['name'])
#     print(fruit['colour'])
#     print(fruit['price'])

# 4.7
# import random
# first_names=[
#     "John",
#     "Amy",
#     "Bob",
#     "Eric"
# ]
# last_names=[
#     "Smith",
#     "Jones",
#     "Booker",
#     "Holmes"
# ]
#
# print(random.choice(last_names))

# Homework 4.2
# chocolates = {
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00,
# }
#
# choice = input("What chocolate would you like? ")
#
# print(chocolates[choice] )

# homework 4.3
import random

ticket = [4, 8, 22, 19, 30, 44, 18]

lotto_numbers = []

for numbers in range(7):
    lotto_numbers.append(random.randint(1, 100))

print("The lotto numbers are: {}".format(lotto_numbers))

matches = 0
prize=0

for number in ticket:
    if number in lotto_numbers:
        matches = matches + 1

if matches == 3:
    prize = "$20"
elif matches == 4:
    prize = "$40"
elif matches == 5:
    prize = "$100"
elif matches == 6:
    prize = "$10000"
elif matches == 7:
    prize = "$1000000"

if prize == 0:
    print("Sorry, you didn't win anything")
else:
    print("You win {}!".format(prize))
