from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://candidate-ro:BRDr#I7d82DcCzJw@candidate-pg.cghvhcfhlix9.eu-central-1.rds.amazonaws.com:5432/candidate"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
