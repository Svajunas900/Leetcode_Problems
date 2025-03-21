"""2115. Find All Possible Recipes from Given Supplies

You have information about n different recipes. 
You are given a string array recipes and a 2D string array ingredients. 
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
"""

def findAllRecipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
  available_supplies = set(supplies)
  ingredient_to_recipes = {}
  in_degree = {}
  recipe_to_ingredients = {}
  
  for i, recipe in enumerate(recipes):
      recipe_ingredients = ingredients[i]
      recipe_to_ingredients[recipe] = recipe_ingredients
      in_degree[recipe] = len(recipe_ingredients)
      
      for ingredient in recipe_ingredients:
          if ingredient not in ingredient_to_recipes:
              ingredient_to_recipes[ingredient] = []
          ingredient_to_recipes[ingredient].append(recipe)
  
  queue = list(available_supplies)
  result = []
  
  while queue:
      current = queue.pop(0)
      
      if current in recipe_to_ingredients:
          result.append(current)
      
      if current in ingredient_to_recipes:
          for dependent_recipe in ingredient_to_recipes[current]:
              in_degree[dependent_recipe] -= 1
              
              if in_degree[dependent_recipe] == 0:
                  queue.append(dependent_recipe)
  
  return result