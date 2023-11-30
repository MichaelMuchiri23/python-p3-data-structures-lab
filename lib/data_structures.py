spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [obj["name"] for obj in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spicy = [obj for obj in spicy_foods if obj["heat_level"] > 5]
    return spicy

def print_spicy_foods(spicy_foods):
    emoji = '\U0001F336'
    for obj in spicy_foods:
        print(f"{obj['name']} ({obj['cuisine']}) | Heat Level: {obj['heat_level'] * emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for obj in spicy_foods:
        if obj["cuisine"] == cuisine:
            return obj

def print_spiciest_foods(spicy_foods):
    emoji = '\U0001F336'
    for obj in spicy_foods:
        if obj["heat_level"] > 5:
            print(f"{obj['name']} ({obj['cuisine']}) | Heat Level: {obj['heat_level'] * emoji}")

def get_average_heat_level(spicy_foods):
    average = 0
    for obj in spicy_foods:
        average += obj["heat_level"]

    return(average / 3)    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

#Case examples
print_spicy_foods(spicy_foods)