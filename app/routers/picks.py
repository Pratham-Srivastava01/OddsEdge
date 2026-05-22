from fastapi import APIRouter
from app.schemas.pick import PickCreate

router=APIRouter(prefix="/picks",tags=["Picks"])


picks_db=[]
next_pick_id=1

@router.get("/")
def get_picks():
    return {"picks":picks_db}

@router.post("/")
def create_pick(pick: PickCreate):
    global next_pick_id

    pick_data = {"id":next_pick_id, **pick.model_dump()}
    picks_db.append(pick_data)
    next_pick_id +=1
    return {"message": "Pick Created", "pick": pick_data}

@router.get("/{pick_id}")
def get_pick(pick_id:int):
    for pick in picks_db:
        if pick["id"]==pick_id:
            return {"pick": pick}
    return {"message": "Pick not found"}

@router.delete("/{pick_id}")
def delete_pick(pick_id:int):
    for pick in picks_db:
        if pick["id"]==pick_id:
            picks_db.remove(pick)
            return {"message": "Pick deleted"}
    return {"message": "Pick not found"}