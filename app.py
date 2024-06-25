from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/prendas_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Prenda

coleccion_prendas = {
    "prendas": [
        {
            "id": 1,
            "tipo": "Remera",
            "marca": "Puma",
            "contexto": "Casual",
            "color": "Roja",
            "precio": "2000"
        },
        {
            "id": 2,
            "tipo": "Pantalón",
            "marca": "Nike",
            "contexto": "Deportivo",
            "color": "Verde",
            "precio": "10000"
        },
        {
            "id": 3,
            "tipo": "Campera",
            "marca": "Levi's",
            "contexto": "Semi-formal",
            "color": "Beige",
            "precio": "20000"
        },
        {
            "id": 4,
            "tipo": "Accesorio",
            "marca": "-",
            "contexto": "Formal",
            "color": "Plateado",
            "precio": "5000"
        },
    ]
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/prendas")
def prendas():
    return render_template('prendas.html', prendas=coleccion_prendas)

@app.route("/agregar_prendas", methods=['POST', 'GET'])
def agregar_prendas():
    if request.method == 'GET':
        return render_template('agregar_prendas.html')
    if request.method == 'POST':
        data = request.form
        tipo = data.get('tipo_prenda')
        marca = data.get('marca_prenda')
        contexto = data.get('contexto_prenda')
        color = data.get('color_prenda')
        precio = data.get('precio_prenda')
        
        prenda_db = Prenda(
            tipo=tipo,
            marca=marca,
            contexto=contexto,
            color=color,
            precio=int(precio)
        )
        
        db.session.add(prenda_db)
        db.session.commit()
        
        new_prenda = {
            "id": len(coleccion_prendas['prendas']) + 1,
            "tipo": tipo,
            "marca": marca,
            "contexto": contexto,
            "color": color,
            "precio": precio
        }
        
        coleccion_prendas.get('prendas').append(new_prenda)
        return redirect('/prendas')

@app.route("/eliminar_prendas", methods=['GET', 'POST'])
def eliminar_prenda():
    if request.method == 'GET':
        prendas_eliminar = coleccion_prendas['prendas']
        return render_template('eliminar_prenda.html', prendas=prendas_eliminar)
    
    if request.method == 'POST':
        prenda_id = int(request.form.get('prenda_id'))
        coleccion_prendas['prendas'] = [prenda for prenda in coleccion_prendas['prendas'] if prenda['id'] != prenda_id]
        return redirect('/prendas')
