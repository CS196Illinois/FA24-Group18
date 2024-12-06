import pandas as pd
import ast
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

# Load the precomputed binary vector CSV file
df = pd.read_csv('vectorized_recipes_binary.csv')  # Update with the actual path if needed
df_mini= pd.read_csv('mini_recipes.csv')

# Convert the 'vectors' column from string representation to lists of integers
df['vectors'] = df['vectors'].apply(lambda x: list(map(int, ast.literal_eval(x))))

# EXTRACTING RAW SET OF ALL INGREDIENTS
# --------------------------------------------------------------
# Collect all unique ingredients
total_ingr = set()
for ingredients_str in df_mini['NER']:
    ingredients_list = ast.literal_eval(ingredients_str)
    total_ingr.update(ingredients_list)

# PROCESSING SET OF ALL INGREDIENTS
# --------------------------------------------------------------
# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Filter out non-food related POS tags and process ingredients
processed_ingr = set()
non_food_pos = {"DET", "PRON", "CCONJ", "SCONJ", "PART", "INTJ"}

for ingredient in total_ingr:
    if len(ingredient) > 2:
        doc = nlp(ingredient)
        if all(token.pos_ not in non_food_pos for token in doc) and not doc[0].is_stop:
            processed_ingr.add(ingredient)

# INPUT NORMALIZER
# --------------------------------------------------------------
def match_ingredients(user_ingredients, total_ingr):
    matched_ingredients = []
    for ingredient in user_ingredients:
        match = process.extractOne(ingredient, total_ingr)
        if match:
            matched_ingredient, score = match
            matched_ingredients.append(matched_ingredient)
    return matched_ingredients  

# USER INPUT
user_ingredients = ["frozn corn", "peper", "cream-cheese", "garlic powder", "butter", "  salt", "mi lk", "o n ions", "dog", "horse", "tomato", "pickles"]
input = match_ingredients(user_ingredients, processed_ingr)

# Generate binary vector for the user input
processed_ingr = sorted(processed_ingr)  # Sort ingredients for consistent indexing
ingredient_to_index = {ingredient: idx for idx, ingredient in enumerate(processed_ingr)}

user_vector = [0] * len(processed_ingr)
for ingredient in input:
    if ingredient in ingredient_to_index:
        user_vector[ingredient_to_index[ingredient]] = 1

# Calculate cosine similarity between the user vector and each recipe's vector
recipe_matrix = df['vectors'].tolist()
similarities = cosine_similarity([user_vector], recipe_matrix).flatten()

# Find the indices of the top 5 most similar recipes
top_5_indices = similarities.argsort()[-5:][::-1]
top_5_scores = similarities[top_5_indices]

# PRINT RESULTS
print("\nTop 5 most similar recipes:")
for rank, (index, score) in enumerate(zip(top_5_indices, top_5_scores), start=1):
    recipe_title = df.iloc[index]['title']
    recipe_directions = df.iloc[index]['directions']
    recipe_ingredients = ast.literal_eval(df_mini.iloc[index]['NER'])

    print(f"\nRecipe {rank}: {recipe_title} (Similarity: {score:.4f})")
    print("Ingredients needed:")
    for ingredient in recipe_ingredients:
        print(f"- {ingredient}")
    print("\nDirections:")
    print(recipe_directions)
    print("------------------------------------------------------------")
