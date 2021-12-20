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
    from model_city import City
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
    """ Finding all City objects """
    cities = my_session.query(City).join(State).order_by(City.id).all()
    """ Print in format """
    for city in cities:
        print("{}: ({}) {}".format(city.state, city.id, city.name))
    """ Close the session """
    my_session.close()
