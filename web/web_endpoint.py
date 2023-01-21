from flask import Flask, render_template, send_from_directory, send_file, request, redirect
from werkzeug.utils import secure_filename
import re
import os
from process import processFile
from threading import Thread
from uuid import uuid4

app = Flask(__name__)

excel_dirs = os.path.join(app.instance_path, "excel_dirs")
os.makedirs(excel_dirs, exist_ok=True)

thread = None

@app.get("/") # getting the template by using GET request
def welcome():
    return render_template("home.html")

dict_to_return = {}

@app.post("/upload")
def uploadData():
    global thread
    f = request.files["file"]
    if (re.match(r"^(.+)(.xlsx)$", f.filename)):
        filepath = os.path.join(excel_dirs, secure_filename(f.filename))
        f.save(filepath)
        thread = Thread(target=processFile, args=(filepath, dict_to_return, ))
        thread.start()
        return redirect("/loading", code=302)
    else:
        return "hanya menerima file .xlsx"

@app.get("/success")
def landingPage():
    return render_template("success.html")

@app.get("/loading")
def loadingPage():
    return render_template("loading.html")

filepath = "Example/example.xlsx"
@app.route("/help")
def help():
    return render_template("help.html", link = "/example_file")


@app.get("/loading_info")
def loading():
    return render_template("loading_info.html", thread_alive = thread.is_alive())

@app.route("/example_file")
def downloadExample():
    return send_file(filepath)

@app.get("/download")
def downloadResult():
    return send_file("results/result.xlsx")
