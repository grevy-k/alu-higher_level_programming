#!/usr/bin/python3
"""
Lists all City objects from the database `hbtn_0e_101_usa`.
Usage: ./list_cities.py <mysql username> <mysql password> <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Unpack command-line arguments
    username, password, db_name = argv[1], argv[2], argv[3]

    # Create the engine and bind it to the session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and their associated State
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

