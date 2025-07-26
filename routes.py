from main import app    
from flask import Flask , render_template

##Rota Homepage
@app.route("/")
def homepage():
    total_categories = len(games_categories)
    total_games = sum(len(games)for games in games_categories.values())
    return render_template("home.html", total_categories= total_categories, total_games = total_games)

## Jogos e categorias
games_categories = {
    "RPG":["sea of stars","undertale","stardew valley", "indivisible"],
    "ação e aventura":["astroneer","eternal strands"],
    "metroidvania":["blasphemous", "hollow knight", "super mombo quest"],
    "plataforma":["celeste", "shovel knight", "dead cells"]
    }

## Rota Jogos
@app.route("/categorias/<nome>")
def game_category(nome):
    nome_formatado = nome.replace("-", " ")
    return render_template("jogos.html", nome=nome_formatado)

## Rota Categorias
@app.route("/categorias")
def all_categories():
    category_list = list(games_categories.keys())
    return render_template('all_categories.html', categories=category_list, games_categories=games_categories)

##Rota Cadastro
@app.route("/cadastro")
def cadastro():
    return render_template("login.html")