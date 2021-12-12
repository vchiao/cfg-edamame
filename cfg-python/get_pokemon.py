# import requests
# from pprint import pprint
#
# pokemon_number = input("What is the Pokemon's ID? ")
# url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
#
# response = requests.get(url)
#
# print(response)
#
# pokemon = response.json()
#
# print(pokemon['height'])
# print(pokemon['weight'])
#
# # pokemon_moves=pokemon['moves']
# # pokemon_move=pokemon_moves['name']
#
# for row in pokemon['moves']:
#     print(row['move']['name'])

#Question 3 homework
import requests

pokemon_list=[5,20,51,30,22]
pokemon_data=[]
# pokemon_info = ""

for each_pokemon in pokemon_list:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(each_pokemon)
    response = requests.get(url)
    pokemon = response.json()

    list_moves = []

    # pokemon_info = pokemon_info + pokemon['name'] + "\n"
    for each_move in pokemon['moves']:
        list_moves.append(each_move['move']['name'])
        # pokemon_info= pokemon_info + "\t" + each_move['move']['name'] + "\n"

    pokemon_data.append({'pokemon name':pokemon['name'],'pokemon moves':list_moves})


with open('pokemon.txt','w+') as pokemon_file:
    pokemon_file.write(str(pokemon_data))

# with open('pokemon.txt','w+') as pokemon_file:
#      pokemon_file.write(pokemon_info)





