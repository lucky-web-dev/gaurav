from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/more")
def more():
    name="Gaurav"
    return render_template("index.html", name=name)
