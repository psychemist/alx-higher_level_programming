#!/usr/bin/python3
'''
contains the class definition of a City object
and an instance Base = declarative_base()
'''
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''
    Defines a class that inherits from Base object
    and links to a MySQL table, with four class attributes
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
