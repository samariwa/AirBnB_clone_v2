#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    __tablename__="amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amentiy')
