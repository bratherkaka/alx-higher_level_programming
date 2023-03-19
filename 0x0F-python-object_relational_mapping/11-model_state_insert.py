#!/usr/bin/python3
"""adds the State object Louisiana to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an instance of the Engine class with the connection information for the database
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, database), pool_pre_ping=True)

    # Create an instance of the sessionmaker class bound to the engine created above
    Session = sessionmaker(bind=engine)

    # Create a session instance by calling the sessionmaker() class
    session = Session()

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session instance
    session.add(new_state)

    # Commit the session to persist changes to the database
    session.commit()

    # Print the new State's id
    print(new_state.id)
