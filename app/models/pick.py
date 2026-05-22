from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Pick(Base):
    __tablename__ = "picks"

    id = Column(Integer, primary_key=True, index=True)
    game = Column(String, nullable=False)
    selection = Column(String, nullable=False)
    sportsbook = Column(String, nullable=False)
    bet_type = Column(String, nullable=False)
    line = Column(Float, nullable=True)
    odds = Column(Integer, nullable=False)
    stake = Column(Float, nullable=False)
    confidence = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)