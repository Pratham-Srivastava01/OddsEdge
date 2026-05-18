from fastapi import APIRouter

router = APIRouter(tags=["refresh"])

@router.post("/refresh")
def refresh_data():
    return {"message": "Refresh endpoint not implemented yet"}