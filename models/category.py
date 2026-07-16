from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True, min_length=2, max_length=50)
    
    # Relationship to books
    books: List["Book"] = Relationship(back_populates="category")