#!/usr/bin/python3
'''
changes the name of a State object from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # establish connection with database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # construct orm query and update State instance object
    session = Session(engine)
    session.query(State).filter(State.id == 2).update(
            {"name": "New Mexico"}, synchronize_session='fetch')

    # save object in database and end DB session
    session.commit()
    session.close()
