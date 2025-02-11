import axiosInstance from "../utils/apiService";
import { ESPNRequest } from "../types/Espn";

export const saveESPNLeague= async (data: ESPNRequest) => {
    if (!data.espn_s2 || !data.league_id || !data.swid || !data.year) {
        throw new Error("Missing ESPN data!")
    }

    const response = await axiosInstance.post('/api/espn/leagues/connect',
        null,
        {
            params: {
                espn_s2: data.espn_s2,
                league_id: data.league_id,
                swid: data.swid,
                year: data.year
            }
        }
    )

    return response.data
}