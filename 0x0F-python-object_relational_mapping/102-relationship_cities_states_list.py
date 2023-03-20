#!/usr/bin/python3
'''
lists all City objects from the database hbtn_0e_101_usa
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
    for city in session.query(City).join(
            State).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()
