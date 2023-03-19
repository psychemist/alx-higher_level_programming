#!/usr/bin/python3
'''
adds the State object “Louisiana” to the database hbtn_0e_6_usa
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # establish connection to database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    # create and add new State instance to table
    louie = State(name="Louisiana")
    session.add(louie)
    session.commit()

    print("{:d}".format(louie.id))

    session.close()
