from fastapi import APIRouter

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.get()
def getReviews():
    pass

@router.post()
def addReviews():
    pass