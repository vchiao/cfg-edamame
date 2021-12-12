# with open('people.txt', 'w+') as text_file:
#     people = 'Joanne \nSusan \nAmina'
#     text_file.write(people)

#5.1
# new_todo=input("Enter your new to-do item: ")
#
# with open("todo.txt", "r") as todo_list:
#     list = todo_list.read()
#
# list = list + "\n" + new_todo
#
# with open("todo.txt","w+") as todo_list:
#     todo_list.write(list)

#5.2
# import csv
#
# with open("trees.csv","r") as file:
#     spreadsheet = csv.DictReader(file)
#
#     heights = []
#
#     for row in spreadsheet:
# #         tree_height = row['height']
#         heights.append(tree_height)
#
# shortest_height = min(heights)
# print(shortest_height)

import requests
