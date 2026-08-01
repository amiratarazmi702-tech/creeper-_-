from flask import Flask, render_template, request, redirect, send_from_directory
import json
import os

app = Flask(__name__)


# صفحه اصلی
@app.route("/")
def home():
    return render_template("index.html")


# نمایش مودها
@app.route("/mods")
def mods():
    with open("mods.json", "r", encoding="utf-8") as file:
        mods = json.load(file)

    return render_template("mods.html", mods=mods)


# ورود مدیریت
@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        password = request.form["password"]

        if password == "322612":
            return render_template("admin.html")

        else:
            return "رمز اشتباه است"


    return render_template("login_admin.html")



# اضافه کردن مود
@app.route("/add_mod", methods=["POST"])
def add_mod():

    new_mod = {
        "name": request.form["name"],
        "image": request.form["image"],
        "description": request.form["description"],
        "version": request.form["version"],
        "price": request.form["price"],
        "file": request.form["file"]
    }


    with open("mods.json", "r", encoding="utf-8") as file:
        mods = json.load(file)


    mods.append(new_mod)


    with open("mods.json", "w", encoding="utf-8") as file:
        json.dump(mods, file, ensure_ascii=False, indent=4)


    return redirect("/mods")



# دانلود واقعی فایل
@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(
        "downloads",
        filename,
        as_attachment=True
    )



if __name__ == "__main__":
    app.run(debug=True)
