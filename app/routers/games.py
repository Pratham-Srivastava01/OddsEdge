from fastapi import APIRouter

router=APIRouter(prefix="/games",tags=["Games"])

@router.get("/")
def get_games():
    return {"games":"[]"}