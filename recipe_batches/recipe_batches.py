# Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have
# available to you, also in the form of a dictionary. Both of these dictionaries will have the same form,
# and might look something like this: { 'eggs': 5, 'butter': 10, 'sugar': 8, 'flour': 15 }
#
# The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe
# dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of
# the ingredients dictionary, the amounts represent the amounts available to you.
#
# Your function should output the maximum number of whole batches that can be made for the supplied recipe using the
# ingredients available to you, as indicated by the second dictionary.
#
# For example:
# # This should return 0 since we don't have enough butter!
# recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# )
#
# Hint: If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
# What's the minimum number of loops we need to perform in order to write a working implementation?
def recipe_batches(recipe_dict, ingredients_dict):
    # Ensure ingredients are sufficient for the recipe
    if len(ingredients_dict) < len(recipe_dict):
        return 0
    batches_list = []
    for item in ingredients_dict:
        if (ingredients_dict[item] - recipe_dict[item]) < 0:
            return 0
        batches_list.append(ingredients_dict[item] // recipe_dict[item])

    # Return int value of batches which would be possible,
    # otherwise 0 for insufficient ingredients.
    return min(batches_list)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
