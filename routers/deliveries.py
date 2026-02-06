from fastapi import APIRouter

router = APIRouter(
    prefix="/deliveries",
    tags=['deliveries']
)

@router.get()
def getDeliveries():
    pass


@router.post()
def addDelivery():
    pass