import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    fecha_suscripcion = Column(DateTime)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    gravity = Column(Integer)
    terrain = Column(String(50))
    surface_water = Column(Integer)
    climate = Column(String(50))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)
    birth_year = Column(Integer)
    species = Column(String(50))
    heigth = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    homeworld = Column(String(50))

class Vehicules(Base):
    __tablename__ = 'vehicules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)
    model = Column(String(50))
    manufacturer = Column(String(50))
    clase = Column(String(50))
    cost = Column(Integer)
    speed = Column(Integer)
    length = Column(Integer)
    cargo_capacity = Column(Integer)
    mimimum_crew = Column(Integer)
    passengers= Column(Integer)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    fecha_guardado = Column(DateTime)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    fecha_guardado = Column(DateTime)

class FavoriteVehicules(Base):
    __tablename__ = 'favorite_vehicules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('vehicules.id'), nullable=False)
    fecha_guardado = Column(DateTime)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
