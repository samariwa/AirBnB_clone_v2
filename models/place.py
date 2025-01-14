#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__="places"
    city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE'),
                    nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                    nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref="place")
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

class place_amenity(BaseModel, Base):
    __tablename__="place_amenity"
    metadata = Base.metadata
    place_id = Column(String(60), ForeignKey('places.id', ondelete='CASCADE'), nullable=False)
    amenity_id = Column(String(60), ForeignKey('amenities.id', ondelete='CASCADE'), nullable=False)

