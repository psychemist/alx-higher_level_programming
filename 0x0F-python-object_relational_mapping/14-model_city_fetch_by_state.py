#!/usr/bin/python3
'''
prints all City objects from the database hbtn_0e_14_usa
'''
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # construct orm query
    session = Session(engine)
    for city in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
