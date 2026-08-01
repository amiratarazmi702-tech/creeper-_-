from flask import Flask, render_template

app = Flask(__name__)

mods = [
    {
        "name": "Football Mod",
        "description": "مود فوتبال ماینکرافت",
        "version": "1.16.5",
        "price": "رایگان"
    },
    {
        "name": "Zombie Mod",
        "description": "مود زامبی",
        "version": "1.16.5",
        "price": "رایگان"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/mods")
def mod_page():
    return render_template("mods.html", mods=mods)


if __name__ == "__main__":
    app.run(debug=True)
