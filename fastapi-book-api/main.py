from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Pydantic model for a book
class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int
    genre: Optional[str] = None
    available: bool = True

#INITIAL SAMPLE DATA
books_db: List[Book] = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", published_year=2008, genre="Programming", available=True),
    Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", published_year=1999, genre="Software Engineering", available=True),
    Book(id=3, title="1984", author="George Orwell", published_year=1949, genre="Dystopian", available=False)
]

# GET ENDPOINT
@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db

# GET ENDPOINT
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# POST ENDPOINT
@app.post("/books/", response_model=Book, status_code=201)
def create_book(book: Book):
    books_db.append(book)
    return book

# PUT ENDPOINT
@app.put("/books/{book_id}", response_model=Book)
def replace_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# PATCH ENDPOINT
@app.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_patch: dict):
    for book in books_db:
        if book.id == book_id:
            updated_data = book.dict()
            updated_data.update(book_patch)
            updated_book = Book(**updated_data)
            books_db[books_db.index(book)] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETION ENDPOINT
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            books_db.remove(book)
            return
    raise HTTPException(status_code=404, detail="Book not found")

# OPTIONS endpoint
@app.options("/books/")
def options_books():
    return {
        "allowed_methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    }
