from main import app    
from flask import Flask , render_template



@app.route("/")
def homepage():
    return "Página incial do site!"

@app.route("/category/<nome>")
def categoria(nome):
   
   games_categories = {
    "RPG":["seaoftears","undertale","masseffect"],
    "Indie":["celeste","stardewvalley","indivisibleswitch","geshinimpact"],
    "Acao&Aventura":["blasphemous","astroneer","eternalstrands"]
   } 

   lista_jogos = games_categories.get(nome , [])
 
   return render_template("category.html", categoria=nome , jogos=lista_jogos)
   
@app.route("/blog")
def blog():
    return render_template("blog.html")