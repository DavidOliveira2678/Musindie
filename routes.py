from main import app    
from flask import Flask , render_template

##Rota Homepage
@app.route("/")
def homepage():
    total_categories = len(games_categories)
    total_games = sum(len(jogos)for jogos in games_categories.values())
    return render_template("home.html", total_categories= total_categories, total_games = total_games)

## Jogos e categorias
games_categories = {
    "RPG":["sea of tears","undertale","mass effect"],
    "Indie":["celeste","stardew valley","indivisible switch","sword of the sea"],
    "acao-aventura":["blasphemous","astroneer","eternal strands"],
    "Corrida":["forza horizon","crash team racing","f1","the crew motorfest"],
    "Luta":["mortal kombat","dragon ball","guilty gear","undisputed","brawlhalla"]
   }

## Rota Categoria de jogo
@app.route("/category/<nome>")

def categoria(nome):
   lista_jogos = games_categories.get(nome , [])
   return render_template("category.html", categoria=nome , jogos=lista_jogos)

## Rota Blog
@app.route("/blog")
def blog():
    return render_template("blog.html")
