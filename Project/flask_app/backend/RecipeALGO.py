import pandas as pd
import ast
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



#EXTRACTING RAW SET OF ALL INGR
#--------------------------------------------------------------

# Load the CSV file
df = pd.read_csv('mini_recipes.csv')  # Update with actual path to the CSV file

# Initialize an empty set to hold all unique ingredients
total_ingr = set()

# Loop through each row in the NER column
for ingredients_str in df['NER']:
    # Convert the string representation of list into an actual list
    ingredients_list = ast.literal_eval(ingredients_str)
    
    # Add each ingredient to the total_ingr set
    total_ingr.update(ingredients_list)






#PROCESSING SET OF ALL INGR
#--------------------------------------------------------------
# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Initialize a new set for processed ingredients
processed_ingr = set()

# Define a list of non-food related POS tags to filter out
non_food_pos = {"DET", "PRON", "CCONJ", "SCONJ", "PART", "INTJ"}

# Loop through each ingredient in total_ingr
for ingredient in total_ingr:
    # Filter out single characters and very short words as nonsensical items
    if len(ingredient) <= 2:
        continue

    # Use spaCy to process the ingredient
    doc = nlp(ingredient)
    
    # Check each token (word) in the ingredient
    if all(token.pos_ not in non_food_pos for token in doc) and not doc[0].is_stop:
        # Add to processed ingredients if it passes checks
        processed_ingr.add(ingredient)




#INPUT NORMALIZER
#--------------------------------------------------------------
from fuzzywuzzy import process 

def match_ingredients(user_ingredients, total_ingr):
    
    matched_ingredients = [] 

    for ingredient in user_ingredients:
        match, score = process.extractOne(ingredient, total_ingr)
        
        matched_ingredients.append(match)

    return matched_ingredients  

user_ingredients = ["frozn corn", "pepper", "cream-cheese", "garlic powder", "stick of butter", "salt", "milk","onions","chocolate sundae syrup", "maraschino cherries", "nuts", "whipped cream", "vanilla ice cream", "strawberry topping", "graham cracker pie crust", "milk"]
input = match_ingredients(user_ingredients, processed_ingr)




#CREATING COLUMN OF VECTORS IN RECIPE DATASET
#--------------------------------------------------------------
# Load the mini_recipes CSV file
df = pd.read_csv('mini_recipes.csv')  # Update with actual path if needed

# Parse the ingredients in the NER column
df['NER'] = df['NER'].apply(ast.literal_eval)  # Convert the string representation of lists to actual lists

# Convert each recipe's ingredients list into a single string for vectorization
df['recipe_string'] = df['NER'].apply(lambda ingredients: " ".join(ingredients))

# Initialize TfidfVectorizer and fit it on the recipes
ingred2vector = TfidfVectorizer()
recipe_matrix = ingred2vector.fit_transform(df['recipe_string'])




#VECTORIZE USER INPUT
#--------------------------------------------------------------
# User input ingredients (as an array of strings) to match against the recipes
user_input = input
user_input_string = " ".join(user_input)  # Join the user input list into a single string

# Transform user input using the fitted vectorizer
user_vector = ingred2vector.transform([user_input_string])

# Get the feature names (ingredient names) for reference
ingredient_names = ingred2vector.get_feature_names_out()

# Calculate cosine similarity between the user input and each recipe
similarities = cosine_similarity(user_vector, recipe_matrix).flatten()

# Find the most similar recipe(s) based on similarity score
most_similar_index = similarities.argmax()
most_similar_score = similarities[most_similar_index]
most_similar_recipe_directions = df.iloc[most_similar_index]['directions']





#PRINT MSGS
#--------------------------------------------------------------
print("\nMost similar recipe:")
print(f"Recipe {most_similar_index + 1}: {df.iloc[most_similar_index]['title']} (Similarity: {most_similar_score:.4f})")

print("\nDirections:")
print(most_similar_recipe_directions)

print("\nUser input vector (raw TF-IDF):")
user_vector_array = user_vector.toarray()[0]
for i, value in enumerate(user_vector_array):
    if value > 0:
        print(f"  Ingredient: {ingredient_names[i]} | TF-IDF: {value:.4f}")
