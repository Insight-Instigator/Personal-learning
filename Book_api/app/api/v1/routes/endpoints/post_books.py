from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.services.book_service import BookService
from app.api.v1.schemas.book import Book, BookCreate
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/", response_model=Book, status_code=201)
async def create_book(book: BookCreate, session: AsyncSession = Depends(get_session)):
    try:
        book_service = BookService(session)
        return await book_service.create_book(book.model_dump())
    except Exception as e:
        logger.error(f"Error in create_book: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error.") 