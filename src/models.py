import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id_u = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(50))

class follower(Base):
    __tablename__ = 'follower'
    f_id = Column(Integer, primary_key=True)
    user_form_id = Column(Integer, ForeignKey('User.id_u'))
    user_to_id = Column(Integer, ForeignKey('User.id_u'))
   
class Comment(Base):
    __tablename__ = 'Comment'
    id_c = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id_u'))
    post_id = Column(Integer, ForeignKey('Post.id_p'))
    
class Post(Base):
    __tablename__ = 'Post'
    id_p = Column(Integer, primary_key=True)
    user_is = Column(Integer, ForeignKey('User.id_u'))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.id_p'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e