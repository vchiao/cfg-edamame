import requests
import csv


def recipe_search(ingredient, exclusion, minutes, health, diet, cuisine):
    app_id = '6cd63dd8'
    app_key = '8fec02f0405453d44f2590d1ef923cbd'
    request_url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)


    for exclude in exclusion:
        request_url = request_url + "&excluded=" + exclude

    for label in health:
        if label != 'None':
            request_url = request_url + "&health=" + label.lower()

    for label in diet:
        if label != 'None':
            request_url = request_url + "&diet=" + label.lower()

    for label in cuisine:
        if  label != 'None' :
            request_url = request_url + "&cuisineType=" + label.lower()

    request_url = request_url + "&minutes=" + minutes

    print(request_url)

    result = requests.get(request_url)
    data = result.json()
    return data['hits']


def get_ingredients_from_input(input):
    temp_list = input.split(", ")
    result = set()

    for item in temp_list:
        result.add(item.strip())

    return result

def save_ingredients_to_file(items_to_save):
    with open('ingredients.csv', 'w+') as csv_file:
        field_names = ['food', 'quantity', 'measure']

        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(items_to_save)
        print('Successfully saved shopping list! Yay!')


def select_ingredient_to_save(results):
    option = int(input("Please select an option (1-10): "))

    if 0 < option <= 10:
        print()
        print("Saving item nr {} with label: {}".format(option, results[option - 1]['recipe']['label']))
        # items to save with unnecessary keys (i.e. wight, foodCategory, image)
        items_to_save = results[option - 1]['recipe']['ingredients']

        items_to_save_stripped = []
        # https://www.geeksforgeeks.org/python-extract-specific-keys-from-dictionary/
        for item in items_to_save:
            items_to_save_stripped.append({key: item[key] for key in item.keys() & {'food', 'quantity', 'measure'}})

        save_ingredients_to_file(items_to_save_stripped)
    else:
        print("Choose number from 1-10")
        select_ingredient_to_save(results)


def ask_for_saving_ingredients(results):
    option = input("Do you want to save ingredients as shopping list? Y/N: ")

    if option == "y" or option == "Y":
        select_ingredient_to_save(results)
    elif option == "n" or option == "N":
        return
    else:
        ask_for_saving_ingredients(results)

# def get_recipes(search_query, cuisine_type, time):
#     app_id = '6cd63dd8'
#     app_key = '8fec02f0405453d44f2590d1ef923cbd'
#     # maximum_cooking_time =1%2B + maximum_cooking_time
#     result = requests.get(
#         'https://api.edamam.com/search?q={}&cuisineType={}&time={}&app_id={}&app_key={}'.format(search_query,
#         cuisine_type, time, app_id, app_key))
#     data = result.json()
#     return data['hits']


def run():
    ingredients = input('Enter ingredient(s) (comma separated): ')
    list_of_ingredients = get_ingredients_from_input(ingredients)

    exclusion = input('Enter different ingredient(s) that you want to exclude (comma separated): ').split(", ")
    minutes = input('Enter max number of minutes you want to spend: ')

    print()

    health_labels = ['None', 'Alcohol-free', 'Dairy-free', 'Gluten-free', 'Keto-friendly', 'Kosher', 'Pescatarian', 'Sugar-conscious', 'Tree-Nut-free', 'Vegan', 'Vegetarian']
    for count, label in enumerate(health_labels):
        print(count, label)
    health = [health_labels[int(x)] for x in input('Filter by health restriction(s) by entering the corresponding number(s) (separate with space): ').split()]

    print()

    diet_labels = ['None', 'Balanced', 'High-Fiber', 'High-Protein', 'Low-Carb', 'Low-Fat', 'Low-Sodium']
    for count, label in enumerate(diet_labels):
        print(count, label)
    diet = [diet_labels[int(x)] for x in input('Filter by diet type(s) by entering the corresponding number(s) (separate with space): ').split()]

    print()

    cuisine_labels = ['None', 'American', 'Asian', 'British', 'Caribbean', 'Central Europe', 'Chinese', 'Eastern Europe', 'French',
               'Indian', 'Italian', 'Japanese', 'Kosher', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic', 'South American', 'South East Asian']
    for count, label in enumerate(cuisine_labels):
        print(count, label)
    cuisine = [cuisine_labels[int(x)] for x in input('Filter by cuisine type(s) by by entering the corresponding number(s)(comma separated): ').split()]


    results = recipe_search(" ".join(list_of_ingredients), exclusion, minutes, health, diet, cuisine)
    index = 1

    print()

    if len(results) > 0:
        for result in results:
            recipe = result['recipe']

            print("{}.".format(index))
            index += 1
            print(recipe['label'])
            print(recipe['url'])
            print('Servings: ' + str(int(recipe['yield'])))
            print('Calories: ' + str(round(recipe['calories'])))
            if(recipe['totalTime']) != 0.0:
                print('Total time: ' + str(int(recipe['totalTime'])) + ' minutes')
            if len(recipe['cautions']) >0:
                print('May contain: ' + ', '.join(recipe['cautions']))

            print()
    else:
        run()

    sort_by = input('Sort results by time/calories: ')
    print()

    recipe_rows = []
    for result in results:
        recipe = result['recipe']
        recipe_row = {
            'Recipe Name': recipe['label'],
            'Ingredients': recipe['ingredientLines'],
            'Cuisine type': recipe['cuisineType'],
            'Time': int(recipe['totalTime']),
            'Calories': int(recipe['calories']),
            'Servings': int(recipe['yield']),
            'URL': recipe['url'],
            'Cautions': recipe['cautions']
        }
        recipe_rows.append(recipe_row)

    if sort_by == 'time':
        sorted_by_time_recipe_rows = sorted(recipe_rows, key=lambda d: d['Time'])
        index = 1
        for result in sorted_by_time_recipe_rows:
            print("{}.".format(index))
            index += 1
            print(result['Recipe Name'])
            print(result['URL'])
            print('Servings: ' + str(int(result['Servings'])))
            print('Calories: ' + str(round(result['Calories'])))
            if (result['Time']) != 0:
                print('Total time: ' + str(int(result['Time'])) + ' minutes')
            if len(result['Cautions']) > 0:
                print('May contain: ' + ', '.join(result['Cautions']))

            print()

    elif sort_by == 'calories':
        sorted_by_calories_recipe_rows = sorted(recipe_rows, key=lambda d: d['Calories'])
        index = 1
        for result in sorted_by_calories_recipe_rows:
            print("{}.".format(index))
            index += 1
            print(result['Recipe Name'])
            print(result['URL'])
            print('Servings: ' + str(int(result['Servings'])))
            print('Calories: ' + str(round(result['Calories'])))
            if (result['Time']) != 0:
                print('Total time: ' + str(int(result['Time'])) + ' minutes')
            if len(result['Cautions']) > 0:
                print('May contain: ' + ', '.join(result['Cautions']))

            print()

    ask_for_saving_ingredients(results)


# Main program
run()