export interface SleeperRequest {
    username?: string
    user_id?: string
    year?: number
    league_id?: string
    week?: string
    league_name?: string
    draft_id?: string
    type?: "add" | "drop"
}

export interface SleeperLeague {
    name: string
    team_name: string
    wins: number
    losses: number
    num_teams: number
}