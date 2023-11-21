#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Class definition for User"""
    __tablename__ = "users"
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
