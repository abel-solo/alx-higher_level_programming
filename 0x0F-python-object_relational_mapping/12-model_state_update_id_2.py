#!/usr/bin/python3
"""
script that changes the name of a State object from the database
3 arguments: mysql username, mysql password and database name
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    statenew = session.query(Statenew).filter_by(id=2).first()
    statenew.name = "New Mexico"

    session.commit()
    session.close()