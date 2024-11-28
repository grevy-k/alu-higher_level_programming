#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter 'a' from the database.
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            dbName
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    session = Session()

    session.query(State).filter(State.name.like("%a%")).\
        delete(synchronize_session='fetch')
    session.commit()

    session.close()
    session.close()
