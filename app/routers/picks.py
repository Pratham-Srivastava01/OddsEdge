from fastapi import APIRouter

router=APIRouter(prefix="/picks",tags=["Picks"])

@router.get("/")
def get_games():
    return {"picks":"[]"}