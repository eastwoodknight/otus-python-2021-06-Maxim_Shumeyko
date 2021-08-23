"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    sessionmaker, scoped_session, declared_attr, 
    declarative_base, relationship,
)


class Base:

    __mapper_args__ = {'eager_defaults': True}

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") \
              or "postgresql+asyncpg://user:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine, cls=Base)

async_session = sessionmaker(
    engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

Session = async_session


class User(Base):
    name = Column(String(64), nullable=False, default="", server_default="")
    username = Column(
        String(64), nullable=False, unique=True, 
        default="", server_default=""
    )
    email = Column(String(64), default="", server_default="")

    posts = relationship(
        "Post", back_populates="user",
#        remote_side="Post.user_id",
#        primaryjoin="User.id==foreign(Post.user_id)",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name}, username={self.username}, "
            f"post={self.email})"
        )

    def __repr__(self):
        return str(self)


class Post(Base):
    title = Column(
        String(256), nullable=False, unique=True, 
        default="", server_default=""
    )
    body = Column(
        Text, nullable=False, 
        default="", server_default=""
    )
    user_id = Column(
        Integer, ForeignKey("blog_users.id"),
        nullable=False, 
    )

    user = relationship(
        "User", back_populates="posts",
#        remote_side="User.id",
#        primaryjoin="Post.user_id==foreign(User.id)",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title}, body={self.body}, "
            f"user_id={self.user_id})"
        )

    def __repr__(self):
        return str(self)
