#from crypt import methods
from cProfile import label
from enum import unique
from unicodedata import name
from flask import Flask, flash ,render_template, request ,redirect, url_for ,session, flash

import psycopg2
import psycopg2.extras
import os
import secrets
import re


app=Flask(__name__)

app.config['SECRET_KEY'] = 'clintoo333david0000'
conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")




@app.route("/")
def home():
    return  render_template("home.html") 



@app.route("/achievements")
def achievement():
    return render_template("achievements.html")

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")     




app.run(debug=True)    