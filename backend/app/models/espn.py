from pydantic import BaseModel, Field, model_validator
from typing import List, Optional
from datetime import datetime

class Player(BaseModel):
    name: str
    playerId: int
    posRank: int # players positional rank
    eligibleSlots: List[str | None] # example ['WR', 'WR/TE/RB']
    lineupSlot: str # the players lineup position
    acquisitionType: str
    proTeam: str # 'PIT' or 'LAR'
    schedule: dict # key is scoring period, example: {'1': {'team': 'LAR', 'date': datetime.datetime(2018, 10, 17, 23, 0)}}
    onTeamId: int # id of fantasy team 
    position: str # main position like 'TE' or 'QB'
    injuryStatus: str
    injured: bool
    total_points: float # players total points during the season
    avg_points: float # players average points during the season
    projected_total_points: float # projected player points for the season
    projected_avg_points: float # projected players average points for the season
    percent_owned: float # percentage player is rostered
    percent_started: float # percentage player is started

class PlayerInfo(BaseModel):
    name: str
    playerId: int
    posRank: int
    lineupSlot: str
    proTeam: str
    position: str
    total_points: float # players total points during the season
    avg_points: float # players average points during the season
    projected_total_points: float # projected player points for the season
    projected_avg_points: float # projected players average points for the season

class PlayerList(BaseModel):
    waiver_wire: List[PlayerInfo]

class DraftPick(BaseModel):
    round_num: int
    round_pick: int
    playerName: str
    team_name: str

class Draft(BaseModel):
    draft: List[DraftPick]

class TeamInfo(BaseModel):
    team_name: str
    wins: int
    losses: int
    ties: int
    team_abbrev: str
    streak_type: str
    streak_length: int
    standing: int
    final_standing: int
    playoff_pct: float

class ESPNTeam(BaseModel):
    team_id: int
    team_abbrev: str
    team_name: str
    division_id: int
    division_name: str
    wins: int
    losses: int
    ties: int
    points_for: float # total points for through out the season
    points_against: float # total points against through out the season
    waiver_rank: int # waiver position
    acquisitions: int # number of acquisitions made by the team
    acquisition_budget_spent: int # budget spent on acquisitions 
    drops: int # number of drops made by the team
    trades: int # number of trades made by the team 
    move_to_ir: int # number of players move to ir
    owners: List[dict] # array of owner dict example: { id: '1234', displayName: 'team', firstName: 'Bob', lastName: 'Joe'} 
    # Note for owners name attributes will only be available for private leagues. Public leagues will not show name data.
    streak_type: str # string of either WIN or LOSS
    streak_length: int # how long the streak is for streak type
    standing: int # standing before playoffs
    final_standing: int # final standing at end of season
    draft_projected_rank: int # projected rank after draft
    playoff_pct: float # teams projected chance to make playoffs
    roster: List[PlayerInfo]

    # These 3 variables will have the same index and match on those indexes
    schedule: List[TeamInfo] = Field(default=None, description="Schedule of opponents")
    scores: List[float]
    outcomes: List[str | None]

class LeagueRankings(BaseModel):
    teams: List[TeamInfo]

class LeagueTeams(BaseModel):
    teams: List[ESPNTeam]

class BoxPlayer(BaseModel):
    name: str
    slot_position: str # the players lineup position
    points: float # points scored in the current week
    projected_points: float # projected points for that week
    pro_opponent: str # the pro team the player is going against
    pro_pos_rank: int # the rank the pro team is against that players position
    game_played: int # 0 (not played/playing) or 100 (finished game)
    game_date: Optional[datetime] # datetime object of when the pro game starts
    on_bye_week: bool # whether or not the player is on a bye
    active_status: str 

class ESPNBoxScore(BaseModel):
    home_team: ESPNTeam
    home_score: int
    home_projected: int
    away_team: ESPNTeam
    away_score: int
    away_projected: int
    home_lineup: List[Player]
    away_lineup: List[Player]
    is_playoff: bool
    matchup_type: str

class TeamScoreboard(BaseModel):
    team_name: str
    team_score: float
    projected: float
    lineup: List[BoxPlayer]

class MatchupScoreboard(BaseModel):
    home_team: TeamScoreboard
    away_team: TeamScoreboard

class WeekScoreboard(BaseModel):
    scores: List[MatchupScoreboard]