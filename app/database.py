from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://musicdb_usga_user:0PZ0dKd8uJCHhIwOvmA5yasi6d3bqWeM@dpg-csfl8908fa8c739vnkhg-a/musicdb_usga"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
