#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
3 arguments: mysql username, mysql password and database name
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # creating an engine for the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine_001 = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine_001)
    session = Session()

    # querying python instances in the database
    for instance in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))

    session.close()
