from fastapi import APIRouter

router = APIRouter()
 
@router.options("/")
def options_books():
    return {
        "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    } 