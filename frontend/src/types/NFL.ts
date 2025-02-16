export interface Game {
    gameid: string
    home_team: Team
    away_team: Team
    total_home_points: number
    total_away_points: number
    start_time: string
    game_type: string
}

export interface Team {
    team_name: string
}