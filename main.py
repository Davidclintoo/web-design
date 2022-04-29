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
conn=psycopg2.connect("dbname='d1m8odf2nbe0jt' user='idlxsyofckzrsu' port='5432 ' host='ec2-52-30-133-191.eu-west-1.compute.amazonaws.com' password='377cc0aab4454edd009635c4786b072f4e75ef0d07fc222ff7020a6c6d950a4a'")
app.config['SECRET_KEY'] = 'clintoo1111david444'
# app.config['SECRET_KEY'] = 'clintoo333david0000'
# conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")




@app.route('/')
def home():
    return  render_template("home.html")

@app.route('/home')
def homes():
    return  render_template("home.html")


@app.route('/achievements')
def achievement():
    return render_template("achievements.html")

@app.route('/about')
def about():
    return render_template("about.html") 

@app.route('/contact')
def contact():
    return render_template("contact.html")     



if __name__ == '__main__':
   app.run(debug=True)    