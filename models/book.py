from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional

def get_utc_now():
    return datetime.now(timezone.utc)

class Book(SQLModel, table=True):
    """Book model for the library database"""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=1, max_length=200)
    author: str = Field(index=True, min_length=1, max_length=100)
    isbn: str = Field(unique=True, index=True)
    published_year: int = Field(ge=1000, le=datetime.now().year)
    available: bool = Field(default=True)
    
    # Foreign key and relationship for Exercise 1
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional["Category"] = Relationship(back_populates="books")
    
    created_at: datetime = Field(default_factory=get_utc_now)
    updated_at: datetime = Field(default_factory=get_utc_now)

class BookCreate(SQLModel):
    """Model for creating a new book"""
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=100)
    isbn: str = Field(min_length=10, max_length=13)
    published_year: int = Field(ge=1000, le=datetime.now().year)
    category_id: Optional[int] = None  # Added for Exercise 1

class BookUpdate(SQLModel):
    """Model for updating a book"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    isbn: Optional[str] = Field(None, min_length=10, max_length=13)
    published_year: Optional[int] = Field(None, ge=1000, le=datetime.now().year)
    available: Optional[bool] = None
    category_id: Optional[int] = None