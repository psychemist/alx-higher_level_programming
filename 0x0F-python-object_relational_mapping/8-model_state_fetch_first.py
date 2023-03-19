#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # construct orm query
    session = Session(engine)
    first = session.query(State).first()
    if first is None:
        print("Nothing\n")
    else:
        print("{}: {}".format(first.id, first.name))

    session.close()
