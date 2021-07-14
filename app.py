import os
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from services import stats, get_character, get_items, get_item, get_all_life, upcoming, get_teams, get_team, get_tournaments, get_player

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# required apikey from https://pandascore.co/
# set API_KEY=9tLPmapXYg3_0qxjjODj-jxSgSPnsfKD1GZHOyX-mFPOa6_HLy0
# twitch key 95n171rhlco6xhc8qadt6p7njeyl2i
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
def index():
    upcmg = upcoming()
    return render_template("main.html", upcmg=upcmg)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print()

    if request.method == "GET":
        return render_template("login.html")


@app.route("/champions")
def champions():
    stat = stats()
    return render_template("champions.html", stat=stat)

@app.route("/character/<name>")
def character(name):
    cha = get_character(name)
    return render_template("character.html", cha=cha[0])


@app.route("/items")
def items():
    items = get_items()
    return render_template("items.html", items=items)


@app.route("/item/<name>")
def item(name):
    itm = get_item(name)
    return render_template("item.html", itm=itm)


@app.route("/live")
def live():
    lives = get_all_life()
    return render_template("live.html", lives=lives)


@app.route("/teams")
def teams():
    teams = get_teams()
    return render_template("teams.html", teams=teams)


@app.route("/team/<name>")
def team(name):
    team = get_team(name)
    print(team)
    return render_template("team.html", team=team[0])


@app.route("/tournaments")
def tournaments():
    tournaments = get_tournaments()
    return render_template("tournaments.html", tournaments=tournaments)


@app.route("/team/player/<name>")
def player(name):
    player = get_player(name)
    return render_template("player.html", player=player[0])