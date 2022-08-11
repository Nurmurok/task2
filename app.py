from crypt import methods
from flask import Flask, render_template, request, redirect
from peewee import *
from models import Monsters

app = Flask(__name__)

@app.route('/')
def home():
    all_monsters = Monsters.select()
    return render_template("index.html", monsters=all_monsters)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method=='POST':
        name = request.form['name']
        description = request.form['description']
        weakness = request.form['weakness']

        Monsters.create(
            name = name,
            description = description,
            weakness = weakness
        )

        return redirect('/')
    return render_template('create.html')

if __name__=="__main__":
    app.run(debug=True)
