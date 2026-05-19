from fastapi import APIRouter
from app.schemas.pick import PickCreate

router=APIRouter(prefix="/picks",tags=["Picks"])

@router.get("/")
def get_games():
    return {"picks":[]}

@router.post("/")
def create_pick(pick: PickCreate):
    return {"message": "Pick Created", "pick": pick.model_dump()}