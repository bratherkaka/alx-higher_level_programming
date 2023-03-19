#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_user, mysql_password, db_name),
                           pool_pre_ping=True)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for all cities and their associated state names
    query = session.query(State, City).filter(State.id == City.state_id).order_by(City.id)

    # Print out the results
    for state, city in query.all():
        print(str(city))
