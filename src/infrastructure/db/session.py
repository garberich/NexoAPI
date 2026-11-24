from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine(database_url: str):
    # check_same_thread only apply if URL start with sqlite, for not breaking create_engine with PostgreSQL or other engines
    connect_args = (
        {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    )
    return create_engine(database_url, connect_args=connect_args)


def get_sessionmaker(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
