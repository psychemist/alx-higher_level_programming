#!/usr/bin/python3
'''
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
'''
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # establish connection to database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # create and add new State instance to table
    with Session() as session:
        new_state = State(name="California")
        new_city = City(name="San Francisco")
        new_state.cities.append(new_city)

        session.add(new_state)
        session.commit()
        session.close()
