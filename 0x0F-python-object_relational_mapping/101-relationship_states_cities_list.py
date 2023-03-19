#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Get database credentials
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to retrieve data
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects with their corresponding City objects
    result = session.query(State).order_by(State.id).all()

    # Print the results
    for state in result:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
