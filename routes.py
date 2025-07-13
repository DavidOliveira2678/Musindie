from main import app    
from flask import Flask , render_template

@app.route("/")
def homepage():
    total_categories = len(games_categories)
    total_games = sum(len(jogos)for jogos in games_categories.values())
    return render_template("home.html", total_categories= total_categories, total_games = total_games)

games_categories = {
    "RPG":["sea_of_tears","undertale","masse_ffect"],
    "Indie":["celeste","stardew_valley","indivisible_switch","geshin_impact"],
    "acao-aventura":["blasphemous","astroneer","eternal_strands"],
    "Corrida":["forza_horizon","crash_team_racing","f1","the_crew_motorfest"],
    "Luta":["mortal_kombat","dragon_ball","guilty_gear","undisputed","brawlhalla"]
   } 
@app.route("/category/<nome>")

def categoria(nome):
   lista_jogos = games_categories.get(nome , [])
   return render_template("category.html", categoria=nome , jogos=lista_jogos)
  
@app.route("/blog")
def blog():
    return render_template("blog.html")
