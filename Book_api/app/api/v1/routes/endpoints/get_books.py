from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_session
from app.services.book_service import BookService
from app.api.v1.schemas.book import Book
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/", response_model=List[Book])
async def get_books(session: AsyncSession = Depends(get_session)):
    try:
        book_service = BookService(session)
        books_list = await book_service.get_all_books()
        
        if not books_list:
            raise HTTPException(status_code=404, detail="No books available.")
        
        return books_list
    except Exception as e:
        logger.error(f"Error in get_books: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error.")

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    try:
        book_service = BookService(session)
        book = await book_service.get_book_by_id(book_id)
        
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        
        return book
    except Exception as e:
        logger.error(f"Error in get_book: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error.") 