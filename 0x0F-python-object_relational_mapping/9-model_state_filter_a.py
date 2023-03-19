#!/usr/bin/python3
"""Start link class to table in database"""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = (session.query(State).filter(State.name.like("%a%")))
    )
    for state in states_with_a:
        print(state.id, state.name, sep = ": ")

