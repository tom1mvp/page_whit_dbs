from app import db

# Creación de tablas
class Prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    contexto = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Prenda {self.tipo} - {self.marca}>' # retorna el tipo de prenda ingresado y la marca