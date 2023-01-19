from flask import Flask, render_template, send_from_directory, send_file, request, redirect
from werkzeug.utils import secure_filename
import re
import os
from process import processFile
from threading import Thread

app = Flask(__name__)

excel_dirs = os.path.join(app.instance_path, "excel_dirs")
os.makedirs(excel_dirs, exist_ok=True)

thread = None

@app.get("/") # getting the template by using GET request
def welcome():
    return render_template("home.html")

@app.post("/upload")
def uploadData():
    global thread
    f = request.files["file"]
    if (re.match(r"^(.+)(.xlsx)$", f.filename)):
        filepath = os.path.join(excel_dirs, secure_filename(f.filename))
        f.save(filepath)
        # processFile(filepath)
        thread = Thread(target=processFile, args=(filepath, ))
        thread.start()
        # return redirect("/success", code=302)
        # while thread.is_alive():
            # landingPage() # show them a landing page
        
        return redirect("/success")
        # return "hello"
        # else give them the result
    else:
        return "hanya menerima file .xlsx"
    
@app.get("/success")
def landingPage():
    while thread.is_alive():
        return render_template("success.html")
    return "hello"

def checkStillAlive():
    return thread.is_alive()

filepath = "Example/example.xlsx"
@app.route("/help")
def help():
    return render_template("help.html", link = "/example_file")

@app.route("/example_file")
def downloadExample():
    return send_file(filepath)