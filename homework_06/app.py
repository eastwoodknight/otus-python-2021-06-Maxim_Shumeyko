import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import BadRequest, InternalServerError

from models.database import db
from models.blogpost import Blogpost
from models.author import Author


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blog.db'

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DB_CONN_URI", "postgresql+psycopg2://user:password@localhost:5432/blog.db"
)
app.config.update(
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')
    

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = Author(name=request.form['author'])
    content = request.form['content']

    post = Blogpost(
        title=title, 
        subtitle=subtitle, 
        author=author, 
        content=content, 
    )

    db.session.add(author)
    db.session.add(post)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest("Error adding post")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError("Database error")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
