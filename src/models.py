import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)

class Api(Base):
    __tablename__ = 'api'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, ForeignKey('favoritos.id'), primary_key=True)
    personajes_id = Column(Integer, ForeignKey('api.id'))
    birth_year = Column(String(250))
    species = Column(String(250))
    heigth = Column(String(250))
    mass = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    homeworld = Column(String(250))

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, ForeignKey('favoritos.id'), primary_key=True)
    planetas_id = Column(Integer, ForeignKey('api.id'))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    gravity = Column(Integer)
    terrain = Column(String(250))
    surface_water = Column(Integer)
    climate = Column(String(250))

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, ForeignKey('favoritos.id'), primary_key=True)
    vehiculos_id = Column(Integer, ForeignKey('api.id'))
    model = Column(String(250))
    manufacturer = Column(String(250))
    clase = Column(String(250))
    cost = Column(Integer)
    speed = Column(Integer)
    length = Column(Integer)
    cargo_capacity = Column(Integer)
    mimimum_crew = Column(Integer)
    passengers = Column(Integer)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
