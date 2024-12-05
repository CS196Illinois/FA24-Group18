# This is our main app file that will load all of our ML models and integrate the frontend and backend 
# We will be using Flask/Django to integrate the frontend with the backend
from flask import Flask, render_template, request, redirect, url_for
from RecipeALGO import RecipeRecommendation


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
        closest_recipe = recipeRec.match_ingredients(data)
        # print(closest_recipe)
        return redirect(url_for('RecipeSuggestion', recipe=closest_recipe))
        
    else:
        return render_template("image_recognition.html")



@app.route("/Recipe_Suggestion")
def RecipeSuggestion():
    recipe = request.args.get('recipe')
    print(recipe)   
    return render_template("RecipeSuggestion.html", data = recipe)



if __name__ == "__main__":
    recipeRec = RecipeRecommendation()
    app.run(debug = True)
    
    
  



