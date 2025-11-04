from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
import os 
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)
# print(f"✅ Connected to {db_url}") -> pentru debugging
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)