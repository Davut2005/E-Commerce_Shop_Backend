from fastapi import APIRouter

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get()
def getOrders():
    pass


@router.post()
def addOrder():
    pass