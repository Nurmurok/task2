from flask import Flask, render_template, request, redirect
from peewee import *
from templates import *
from models import *
app = Flask(__name__)

import requests
import json
    

@app.route('/')
def home():
    all_countriess = Data.select()
    response= requests.get('https://restcountries.com/v3.1/all')
    text = response.json()
    for i in range(20):
        name =text[i]['name']['common']
        official_name =text[i]['name']['official']
        capital =text[i]['capital'][0]
        region =text[i]['region']
        subregion = text[i]['subregion']
        population = text[i]['population']
        continents = text[i]['continents'][0]
        timezones = text[i]['timezones'][0]
        flag = text[i]['flags']['png']
    
        Data.create(
            name=name,
            official_name=official_name,
            capital=capital,
            region=region,
            subregion=subregion,
            population=population,
            continents=continents,
            timezones=timezones,
            flag = flag
        )
    return render_template("index.html", data=all_countriess)

    
if __name__=="__main__":
    app.run(debug=True)
