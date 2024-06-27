#!/usr/bin/python3
"""
    Updates the name of a State object from the database hbtn_0e_6_usa
    where id = 2 to 'New Mexico'
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

    # Retrieve the state with id = 2
    to_modify = session.get(State, 2)
    
    # Update the state's name if it exists
    if to_modify:
        to_modify.name = 'New Mexico'
        session.commit()

    # Clean up
    session.close()

