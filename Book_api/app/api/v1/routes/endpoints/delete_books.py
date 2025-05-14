from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.services.book_service import BookService
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int, session: AsyncSession = Depends(get_session)):
    try:
        book_service = BookService(session)
        if not await book_service.delete_book(book_id):
            raise HTTPException(status_code=404, detail="Book not found.")
    except Exception as e:
        logger.error(f"Error in delete_book: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error.") 