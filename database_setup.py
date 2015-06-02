# configuration code GREEN

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# class definition PURPLE
class Restaurant(Base):
    
    # table info YELLOW
    __tablename__ = 'restaurant'
    
    # mapper PINK
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

# class definition PURPLE
class MenuItem(Base):
    # table info YELLOW
    __tablename__ = 'menu_item'

    # mapper PINK
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



# configuration code GREEN

engine = create_engine('sqlite:///restaurantMenu.db')

Base.metadata.create_all(engine)