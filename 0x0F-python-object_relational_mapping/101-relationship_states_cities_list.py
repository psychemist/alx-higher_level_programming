#!/usr/bin/python3
'''
lists all State objects, and corresponding City objects
contained in the database hbtn_0e_101_usa
'''
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    # establish connection to database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    # query ORM and list all state and city instances
    for state in session.query(State).outerjoin(
            City).order_by(State.id, City.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.commit()
    session.close()
