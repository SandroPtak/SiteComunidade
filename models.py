from main import database
from datetime import datetime

#Criação do modelo das tabelas do banco de dados


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg', nullable=False)
    posts = database.relationship('Post', backref='autor', lazy=True)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    tema = database.Column(database.String, nullable=False, default='Comunicado')
    imagem = database.Column(database.String)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
