#!/usr/bin/python3
"""
Script that lists all State objects from database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    """ Importing modules """
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    """ Variables representing arguments """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    """ Start engine """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    """ Create a configured class Session """
    Session = sessionmaker(bind=engine)
    """ Setting up session """
    session = Session()
    """ Changing name of object with 2 as it's id """
    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    """ Commit new state """
    session.commit()
    """ Session closed """
    session.close()
