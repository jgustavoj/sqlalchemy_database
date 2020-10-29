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
<<<<<<< HEAD
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
=======
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    #primary key? foreignkey? for email

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))

# class Media(Base):
#     __tablename__= 'Media'
#     id = Column(Integer, primary_key=(True))
#     media_type = Column(enumerate(250), nullable=False )
#     url = Column(String(250), nullale = True )
#     post_id = (Integer, ForeignKey('Post.id'))

# class Follower(Base):
#     __tablename__='Follower'
#     user_from_id = Column(Integer, nullable=False )
#     user_to_id = Column(Integer, nullable=False )
>>>>>>> ee6a873896d9b022b2790955ba7cf6dc2b8456f3


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