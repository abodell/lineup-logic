from pydantic import BaseModel, Field
from typing import List

class ESPNPlayer(BaseModel):
    name: str
    playerId: int
    posRank: int # players positional rank
    eligibleSlots: List[str] # example ['WR', 'WR/TE/RB']
    lineupSlot: str # the players lineup position
    acquisitionType: str
    proTeam: str # 'PIT' or 'LAR'
    schedule: dict # key is scoring period, example: {'1': {'team': 'LAR', 'date': datetime.datetime(2018, 10, 17, 23, 0)}}
    onTeamId: int # id of fantasy team 
    position: str # main position like 'TE' or 'QB'
    injuryStatus: str
    injured: bool
    total_points: int # players total points during the season
    avg_points: int # players average points during the season
    projected_total_points: int # projected player points for the season
    projected_avg_points: int # projected players average points for the season
    percent_owned: int # percentage player is rostered
    percent_started: int # percentage player is started
    stats: dict # holds each week stats, actual and projected points. 

class ESPNTeam(BaseModel):
    team_id: int
    team_abbrev: str
    team_name: str
    division_id: str
    division_name: str
    wins: int
    losses: int
    ties: int
    points_for: int # total points for through out the season
    points_against: int # total points against through out the season
    waiver_rank: int # waiver position
    acquisitions: int # number of acquisitions made by the team
    acquisition_budget_spent: int # budget spent on acquisitions 
    drops: int # number of drops made by the team
    trades: int # number of trades made by the team 
    move_to_ir: int # number of players move to ir
    owners: List[dict] # array of owner dict example: { id: '1234', displayName: 'team', firstName: 'Bob', lastName: 'Joe'} 
    # Note for owners name attributes will only be available for private leagues. Public leagues will not show name data.
    stats: dict # holds teams season long stats
    streak_type: str # string of either WIN or LOSS
    streak_length: int # how long the streak is for streak type
    standing: int # standing before playoffs
    final_standing: int # final standing at end of season
    draft_projected_rank: int # projected rank after draft
    playoff_pct: int # teams projected chance to make playoffs
    logo_url: str
    roster: List[ESPNPlayer]

    # These 3 variables will have the same index and match on those indexes
    schedule: List["ESPNTeam"] = Field(default=None, description="Schedule of opponents")
    scores: List[int]
    outcomes: List[str]

ESPNTeam.model_rebuild()

class ESPNBoxScore(BaseModel):
    home_team: ESPNTeam
    home_score: int
    home_projected: int
    away_team: ESPNTeam
    away_score: int
    away_projected: int
    home_lineup: List[ESPNPlayer]
    away_lineup: List[ESPNPlayer]
    is_playoff: bool
    matchup_type: str

class TeamScoreboard(BaseModel):
    team_name: str
    team_score: float
    projected: float

class MatchupScoreboard(BaseModel):
    home_team: TeamScoreboard
    away_team: TeamScoreboard

class WeekScoreboard(BaseModel):
    scores: List[MatchupScoreboard]