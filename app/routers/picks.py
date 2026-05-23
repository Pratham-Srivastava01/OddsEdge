from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.pick import Pick
from app.schemas.pick import PickCreate
from app.schemas.pick import PickResponse

router=APIRouter(prefix="/picks",tags=["Picks"])


@router.get("/", response_model=list[PickResponse])
def get_picks(db: Session = Depends(get_db)):
    picks = db.query(Pick).all()
    return {"picks":picks}

@router.post("/", response_model=PickResponse)
def create_pick(pick: PickCreate, db: Session = Depends(get_db)):
    db_pick=Pick(**pick.model_dump())
    db.add(db_pick)
    db.commit()
    db.refresh(db_pick)
    return {"message": "Pick Created", "pick": db_pick}

@router.get("/{pick_id}", response_model=PickResponse)
def get_pick(pick_id: int, db: Session = Depends(get_db)):
    pick = db.query(Pick).filter(Pick.id == pick_id).first()

    if pick is None:
        return {"message": "Pick not found"}

    return {"pick": pick}

@router.delete("/{pick_id}")
def delete_pick(pick_id: int, db: Session = Depends(get_db)):
    pick = db.query(Pick).filter(Pick.id == pick_id).first()

    if pick is None:
        return {"message": "Pick not found"}

    db.delete(pick)
    db.commit()

    return {"message": "Pick deleted"}

@router.put("/{pick_id}", response_model=PickResponse)
def update_pick(pick_id: int, pick_update: PickCreate, db:Session=Depends(get_db)):
    pick=db.query(Pick).filter(Pick.id==pick_id).first()

    if pick is None:
        return {"message": "Pick not found"}
    
    pick.game = pick_update.game
    pick.selection = pick_update.selection
    pick.sportsbook = pick_update.sportsbook
    pick.bet_type = pick_update.bet_type
    pick.line = pick_update.line
    pick.odds = pick_update.odds
    pick.stake = pick_update.stake
    pick.confidence = pick_update.confidence
    pick.notes = pick_update.notes

    db.commit()
    db.refresh(pick)

    return pick