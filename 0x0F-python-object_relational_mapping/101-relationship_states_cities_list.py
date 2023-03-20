#!/usr/bin/python3
'''
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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

    # create and add new State instance to table
    for state in session.query(State).join(
            City).order_by(State.id, City.id).all():
        print("{:d}: {:s}".format(state.id, state.name))
        for city in state.cities:
            print("\t{:d}: {:s}".format(city.id, city.name))

    session.commit()
    session.close()
