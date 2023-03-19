#!/usr/bin/python3
"""Script that lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    # Set up connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query for all City objects and their associated State objects
    cities = session.query(City).order_by(City.id).all()
    
    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
