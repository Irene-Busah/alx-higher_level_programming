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
    my_session = Session()
    """ Printing state objects """
    for object in my_session.query(State).filter(State.name.like('%a%')).all():
        print("{}: {}".format(object.id, object.name))
    """ Session closed """
    my_session.close()
