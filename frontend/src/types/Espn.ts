export interface ESPNRequest {
    league_id?: string
    espn_s2?: string
    year?: number
    swid?: string
    user_id?: string
    team_name?: string
    owner_id?: string
}

export interface ESPNLeague {
    name: string
    team_name: string
    wins: number
    losses: number
    num_teams: number
}