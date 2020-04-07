from flask import Flask, render_template
app=Flask(__name__,template_folder='template')
@app.route("/")
def index():
    headline="Hello! World."
    return render_template("in.html",headl=headline)
