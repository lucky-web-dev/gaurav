import datetime
from flask import Flask, render_template
app=Flask("__name__",template_folder='template')
@app.route("/")
def index():
    x=datetime.datetime.now()
    year=(x.month==1 and x.day==1)
    return render_template("ind.html",y=year)
