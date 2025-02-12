from pydantic import BaseModel

class SleeperLeague(BaseModel):
    name: str
    num_teams: int
    wins: int
    losses: int
    team_name: str