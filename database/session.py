import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Ensure the database URL is present before trying to boot
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")

# Create the engine with connection pooling safety
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    # pool_pre_ping checks if connection is alive before handing it to a request
    pool_pre_ping=True  
)

def get_session():
    """Dependency for getting a database session"""
    with Session(engine) as session:
        yield session