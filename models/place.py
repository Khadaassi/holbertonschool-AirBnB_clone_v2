#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity_table = Table("place_amenity",
                                Base.metadata,
                                Column(
                                    "place_id",
                                    String(60),
                                    ForeignKey("places.id"),
                                    primary_key=True,
                                    nullable=False
                                    ),
                                Column(
                                    "amenity_id",
                                    String(60),
                                    ForeignKey("amenities.id"),
                                    primary_key=True,
                                    nullable=False
                                    )
                                )


class Place(BaseModel, Base):
    """ Defines Place class """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="place",
                               cascade="all, delete", passive_deletes=True)

        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False, backref="place_amenity")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """ Return Reviews list """
            list_reviews = []

            for value in models.storage.all(Review).values():
                if value.place_id == self.id:
                    list_reviews.append(value)

            return list_reviews

        @property
        def amenities(self):
            """ Return Amenities list """
            list_amenities = []

            for value in models.storage.all(Amenity).values():
                if value.place_id == self.id:
                    list_amenities.append(value)

            return list_amenities

        @amenities.setter
        def amenities(self, cls):
            """ Amenity id """
            if not isinstance(cls, Amenity):
                return
            self.amenity_ids.append(cls.id)
