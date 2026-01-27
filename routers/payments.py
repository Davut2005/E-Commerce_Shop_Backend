from fastapi import APIRouter

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)

@router.get()
def getPayments():
    pass