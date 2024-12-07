# This is our main app file that will load all of our ML models and integrate the frontend and backend 
# We will be using Flask/Django to integrate the frontend with the backend
from flask import Flask, render_template, request, redirect, url_for
from algo2 import recommend_recipe3


UPLOAD_FOLDER = 'uploads'
app = Flask(__name__, static_folder='static')


@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/image_upload")
def image_upload():
    
    return render_template("ImageUpload.html")

# @app.route("/upload", methods=["POST", "GET"])
# def upload():
#     file = request.files['file']
#     file.save(f'uploads{file.filename}')
#     return redirect('/image_recognition')



@app.route("/image_recognition", methods = ["POST", "GET"])
def image_recognition():
    if request.method  == "POST":
        data = request.get_json()
        closest_recipe = recommend_recipe3(data)
        # print(closest_recipe)
        return redirect(url_for('RecipeSuggestion', recipe=closest_recipe))
        
    else:
        return render_template("image_recognition.html")



@app.route("/Recipe_Suggestion")
def RecipeSuggestion():
    recipe = request.args.get('recipe')
    print(recipe)   
    return render_template("RecipeSuggestion.html", data = recipe)


@app.route('/process_ingredients', methods=['POST'])
def process_ingredients():
    data = request.get_json()

    if data is None:  # Handle the case where no data is sent
        return "No data received", 400

    print(f"Received data: {data}")
    user_ingredients = data if isinstance(data, list) else []

    # Assume `recommend_recipe` returns a list of concatenated strings (recipe + ingredients + directions)
    recipe_packages = recommend_recipe3(user_ingredients)

    print(f"Processed ingredients: {user_ingredients}")
    print(f"Recommended recipes: {recipe_packages}")

    # Render the template with the list of recipe packages
    return render_template(
        'ProcessedData.html',
        ingredients=user_ingredients,
        recipes=recipe_packages  # Pass the full list of recipe packages
    )



if __name__ == "__main__":
    app.run(debug = True)
    
    
  



