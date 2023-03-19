#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # read mysql username, password and database name from input arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # setup engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_user, mysql_pwd, db_name),
                           pool_pre_ping=True)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # update state with id=2 to have name 'New Mexico'
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()

    # close session
    session.close()
