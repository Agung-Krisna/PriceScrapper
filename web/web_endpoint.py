from flask import Flask, render_template, send_from_directory, send_file, request

app = Flask(__name__)

@app.get("/") # getting the template by using GET request
def welcome():
    return render_template("home.html")

@app.post("/")
def process_data():
    return "Hello"

filepath = "Example/example.xlsx"
@app.route("/help")
def help():
    return render_template("help.html", link = "/example_file")

@app.route("/example_file")
def downloadExample():
    return send_file(filepath)