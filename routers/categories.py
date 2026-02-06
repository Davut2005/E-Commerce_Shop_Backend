from fastapi import APIRouter

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get()
def getCategories():
    pass


@router.post()
def addCategory():
    pass