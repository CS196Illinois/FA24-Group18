import pandas as pd
import ast
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

def recommend_recipe3(user_ingredients):
    # Load precomputed binary vector CSV file
    df = pd.read_csv('vectorized_recipes_binary.csv')  # Update the path as needed
    df_mini = pd.read_csv('mini_recipes.csv')

    # Convert 'vectors' column to lists of integers
    df['vectors'] = df['vectors'].apply(lambda x: list(map(int, ast.literal_eval(x))))

    # Extract all unique ingredients from the dataset
    total_ingr = set()
    for ingredients_str in df_mini['NER']:
        ingredients_list = ast.literal_eval(ingredients_str)
        total_ingr.update(ingredients_list)

    # Load spaCy's English model
    nlp = spacy.load("en_core_web_sm")
    non_food_pos = {"DET", "PRON", "CCONJ", "SCONJ", "PART", "INTJ"}

    # Process ingredients to filter out non-food items
    processed_ingr = set()
    for ingredient in total_ingr:
        if len(ingredient) > 2:
            doc = nlp(ingredient)
            if all(token.pos_ not in non_food_pos for token in doc) and not doc[0].is_stop:
                processed_ingr.add(ingredient)

    # Match user input ingredients to the processed ingredient set
    def match_ingredients(user_ingredients, total_ingr):
        matched_ingredients = []
        for ingredient in user_ingredients:
            match = process.extractOne(ingredient, total_ingr)
            if match:
                matched_ingredient, score = match
                matched_ingredients.append(matched_ingredient)
        return matched_ingredients

    # Match user ingredients to dataset ingredients
    input_ingredients = match_ingredients(user_ingredients, processed_ingr)

    # Generate binary vector for the user's input
    processed_ingr = sorted(processed_ingr)  # Ensure consistent indexing
    ingredient_to_index = {ingredient: idx for idx, ingredient in enumerate(processed_ingr)}

    user_vector = [0] * len(processed_ingr)
    for ingredient in input_ingredients:
        if ingredient in ingredient_to_index:
            user_vector[ingredient_to_index[ingredient]] = 1

    # Calculate cosine similarity between user vector and recipe vectors
    recipe_matrix = df['vectors'].tolist()
    similarities = cosine_similarity([user_vector], recipe_matrix).flatten()

    # Find the top 3 most similar recipes
    top3_indices = similarities.argsort()[-3:][::-1]

    # Retrieve recipe details for the top 3 matches
    result = []
    for index in top3_indices:
        recipe_title = df.iloc[index]['title']
        recipe_ingredients = ", ".join(ast.literal_eval(df_mini.iloc[index]['NER']))
        recipe_directions = " ".join(ast.literal_eval(df.iloc[index]['directions']))
        formatted_recipe = f"{recipe_title}\nIngredients: {recipe_ingredients}\nDirections: {recipe_directions}"
        result.append(formatted_recipe)

    # Return the result as a list of 3 strings
    return result

# Example usage
user_ingredients = ["onion", "garlic", "potato", "rice", "lemon", "salt", "pepper", "chicken", "oil", "beans", "butter", "clam", "corn", "flour"]
res = recommend_recipe3(user_ingredients)
for recipe in res:
    print(recipe)
    print("\n---\n")
