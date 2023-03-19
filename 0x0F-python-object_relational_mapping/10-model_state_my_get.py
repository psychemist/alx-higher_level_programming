#!/usr/bin/python3
'''
prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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

    # construct orm query
    session = Session(engine)
    valid = session.query(State).filter(State.name == argv[4]).all()
    if not valid:
        print("Not found")
    else:
        print("{}".format(valid[0].id))

    session.close()
