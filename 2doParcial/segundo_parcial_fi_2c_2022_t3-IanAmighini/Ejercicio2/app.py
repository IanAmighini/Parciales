from flask import Flask, render_template

app=Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.get('/clientes/')
def get_resultados():
    return render_template('clientes.html')