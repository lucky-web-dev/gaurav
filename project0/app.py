
from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route("/")
def index():
    n=["Gaurav", "Lucky", "Again"]
    return render_template("in.html",name=n)
