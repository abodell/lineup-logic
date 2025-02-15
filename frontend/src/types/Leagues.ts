import { ESPNLeague } from "./Espn"
import { SleeperLeague } from "./Sleeper"

export interface LeaguesRequest {
    user_id?: string
}

export interface League {
    espn: ESPNLeague[]
    sleeper: SleeperLeague[]
}