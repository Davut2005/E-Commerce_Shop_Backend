from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get()
def getUsers():
    pass


@router.post()
def addUser():
    pass

