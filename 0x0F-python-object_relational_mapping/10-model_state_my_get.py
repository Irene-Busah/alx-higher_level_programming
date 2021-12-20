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
    state_name = argv[4]
    """ Start engine """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    """ Create a configured class Session """
    Session = sessionmaker(bind=engine)
    """ Setting up session """
    my_session = Session()
    """ Printing state objects """
    object = my_session.query(State).filter(
        State.name == state_name).first()
    if object:
        print("{}".format(object.id))
    else:
        print("Not found")
    """ Session closed """
    my_session.close()
