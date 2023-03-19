#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” from the database
hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create a connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California"
    ca = State(name="California")
    session.add(ca)

    # Create the City "San Francisco"
    sf = City(name="San Francisco", state=ca)
    session.add(sf)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
