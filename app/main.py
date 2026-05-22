from fastapi import FastAPI
from app.routers import health,games,picks,refresh
from app.db.base import Base
from app.db.session import engine
from app.models.pick import Pick



app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Sports Betting API Is Running!"}

app.include_router(health.router)
app.include_router(games.router)
app.include_router(picks.router)
app.include_router(refresh.router)