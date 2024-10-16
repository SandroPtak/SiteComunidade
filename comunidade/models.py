from comunidade import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

#Criação do modelo das tabelas do banco de dados


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg', nullable=False)
    posts = database.relationship('Post', backref='autor', lazy=True)
    comentarios = database.relationship('Comentario', backref='autor_comentario', lazy=True)

    def contar_posts(self):
        return len(self.posts)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    tema = database.Column(database.String, nullable=False, default='Comunicado')
    imagem = database.Column(database.String)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    comentarios_post = database.relationship('Comentario', backref='comentarios_do_post', lazy=True)


class Comentario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    texto_comentario = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario_comentario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    id_post = database.Column(database.Integer, database.ForeignKey('post.id'), nullable=False)
