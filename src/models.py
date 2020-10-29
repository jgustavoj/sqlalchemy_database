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
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False, unique=False)
    lastname = Column(String(250), nullable=False, unique=False)
    email = Column(String(250), nullable=False, unique=True)

class Follower(Base):
    __tablename__='Follower'
    id = Column(Integer, primary_key=True)
    follower = Column(Integer, ForeignKey('User.id'), nullable=False, unique=False)
    followed = Column(Integer, ForeignKey('User.id'), nullable=False, unique=False)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False, unique=False)

class Media(Base):
    __tablename__= 'Media'
    id = Column(Integer, primary_key=True)
    media_type = Column(String(250), nullable=False, unique=False)
    url = Column(String(250), nullable=True, unique=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False, unique=False)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    comment_text = Column(String(250), nullable=False, unique=False)
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False, unique=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False, unique=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)