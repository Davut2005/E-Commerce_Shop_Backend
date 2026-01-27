from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get()
def getProducts():
    pass