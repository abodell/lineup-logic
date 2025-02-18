import { Team } from "./NFL"

export interface BettingGame {
    away_line: number
    away_ml: number
    away_spread: number
    home_line: number
    home_ml: number
    home_spread: number
    over_line: number
    total: number
    under_line: number
    game: BettingTeam
}

export interface BettingTeam {
    away_team: Team
    away_team_id: string
    home_team: Team
    home_team_id: string
    start_time: string
}