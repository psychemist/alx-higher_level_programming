#!/usr/bin/python3
'''
adds the State object “Louisiana” to the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # open new database session
    session = Session(engine)

    # create and add new State object
    louie = State(id=6,
                  name="Louisiana")
    session.add(louie)
    session.commit()
    print(louie.id)

    session.close()
