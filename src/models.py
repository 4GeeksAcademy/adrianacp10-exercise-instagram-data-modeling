import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


##el back_populate se hace para mantener relaciones bidireccionales entre las tablas
class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False)
    firstname = Column(String(120), nullable=False)
    lastname = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(80), nullable=False)

    posts = relationship('Post', back_populates = 'user')
    comments = relationship('Comment', back_populates='user')


class Post(Base):
    __tablename__ = 'post'

    id_post = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id.user'))

    user = relationship('User', back_populates ='posts')
    comments = relationship('Comment', back_populates ='post')


class Followers(Base):
    __tablename__ = 'followers'

    id_followers = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id_user'))
    user_from_id = Column(Integer, ForeignKey('user.id_user'))

    user_to = relationship('User', ForeignKeys =[user_to_id])
    user_from = relationship('User', Foreign_keys = [user_from_id])
    
class Comment(Base):
    __tablename__ = 'comment'

    id_comment = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id_user'))
    post_id = Column(Integer, ForeignKey('post.id.post'))

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
