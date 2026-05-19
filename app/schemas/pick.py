from typing import Optional, Literal
from pydantic import BaseModel, Field


class PickCreate(BaseModel):
    game:str= Field(..., min_lenght=3, max_lenght=100, description="The name of the Game/Matchup")
    selection: str= Field(..., min_length=2, max_length=100, description= "Selected Team/Side")
    sportsbook: str=Field(..., min_length=2, max_length=50, description="Site/Company to find this play")
    bet_type: Literal["Moneyline", "Spread", "Total"] = Field(..., description="Type of bet being placed")
    line: Optional[float] = Field(default=None, description="Spread or total line, e.g. -3.5 or 45.5")
    odds: int= Field(...,description="American Odds, i.e -110 or +150" )
    stake: float=Field(..., gt=0, description="Amount of money being wagered")
    confidence: int=Field(..., ge=1, le=10, description="Confidence level of the pick, 1-10")
    notes: Optional[str]=Field(default=None, max_length=250, description="Additional notes or reasoning behind the pick")