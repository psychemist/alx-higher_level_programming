#!/usr/bin/python3
'''
contains the class definition of a State object
and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''
    Defines a class that inherits from SQLAlchemy Base object
    and links to a MySQL table, with three class attributes
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all,delete")
