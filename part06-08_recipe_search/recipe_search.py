# This function reads a text file of recipes and turns them into a list of recipe dictionaries.
def parse_recipes(filename: str):
    # Open the file and read each line, removing any extra spaces at the beginning or end.
    with open(filename) as file:
        lines = [line.strip() for line in file]
    
    recipes = []  # This will hold all the recipes we find.
    i = 0  # This is our index to go through the lines one by one.
    
    while i < len(lines):  # Keep going as long as we have more lines to read.
        if lines[i] == "":  # Skip empty lines.
            i += 1
            continue
        
        name = lines[i]  # First line is the name of the recipe.
        prep_time = int(lines[i+1])  # Next line is the prep time, which we turn into a number.
        
        ingredients = []  # Start a new list to hold the ingredients.
        i += 2  # Move past the name and prep time.
        
        # Keep reading ingredients until we hit an empty line (end of recipe).
        while i < len(lines) and lines[i] != "":
            ingredients.append(lines[i])
            i += 1
        
        # Save the recipe as a dictionary with name, prep time, and ingredient list.
        recipes.append({
            "name": name,
            "prep_time": prep_time,
            "ingredients": ingredients
        })
    
    return recipes  # Return the full list of recipes.

# This function searches for recipes whose names include a given word.
def search_by_name(filename: str, word: str):
    word = word.lower()  # Make the word lowercase so the search isn't case-sensitive.
    recipes = parse_recipes(filename)  # Get the list of recipes.
    
    # Return the names of recipes that contain the search word.
    return [recipe["name"] for recipe in recipes if word in recipe["name"].lower()]

# This function finds recipes that can be made in a certain amount of time or less.
def search_by_time(filename: str, prep_time: int):
    recipes = parse_recipes(filename)  # Get the list of recipes.
    
    # Return the name and prep time for recipes that are quick enough.
    return [f'{recipe["name"]}, preparation time {recipe["prep_time"]} min'
            for recipe in recipes if recipe["prep_time"] <= prep_time]

# This function searches for recipes that use a specific ingredient.
def search_by_ingredient(filename: str, ingredient: str):
    ingredient = ingredient.lower()  # Make the ingredient lowercase for consistent search.
    recipes = parse_recipes(filename)  # Get the list of recipes.
    
    # Return recipes that use the given ingredient (case-insensitive match).
    return [f'{recipe["name"]}, preparation time {recipe["prep_time"]} min'
            for recipe in recipes if ingredient in map(str.lower, recipe["ingredients"])]
