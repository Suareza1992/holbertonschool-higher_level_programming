#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    Deletes all State objects with a name containing the letter 'a'
    from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command-line arguments
    user, passwd, db_name = sys.argv[1:4]

    # Create an engine and bind it to the metadata of the Base class
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db_name}')
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Retrieve all states with a name containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the states
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Clean up
    session.close()
