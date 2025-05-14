from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.services.book_service import BookService
from app.api.v1.schemas.book import Book, BookUpdate
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate, session: AsyncSession = Depends(get_session)):
    try:
        book_service = BookService(session)
        updated_book = await book_service.update_book(book_id, book.model_dump(exclude_unset=True))
        
        if not updated_book:
            raise HTTPException(status_code=404, detail="Book not found.")
        
        return updated_book
    except Exception as e:
        logger.error(f"Error in update_book: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error.") 