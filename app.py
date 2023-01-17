from flask import Flask
from flask import render_template as rt

app = Flask(__name__)

@app.get('/fizzbuzz')
def fizzbuzz():
    return rt('index.html')