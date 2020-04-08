from flask import Flask, render_template
app=Flask("__name__",template_folder='template')
@app.route("/")
def index():
    n="gaurav"
    return render_template("index.html",name=n)
