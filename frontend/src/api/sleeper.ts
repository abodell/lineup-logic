import axiosInstance from "../utils/apiService";
import { SleeperRequest } from "../types/Sleeper";

export const saveSleeperUser = async (data: SleeperRequest) => {
    if (!data.username) {
        throw new Error('Username is required')
    }
    
    const response = await axiosInstance.post('/api/sleeper/user', 
        null,
        {
            params: {
                username: data.username,
                year: data.year
            }
        }
    )
    return response.data
}

export const getSleeperInfo = async (data: SleeperRequest) => {
    if (!data.user_id) {
        throw new Error("User ID required")
    }

    const response = await axiosInstance.get(`/api/sleeper/userinfo/${data.user_id}`)

    return response.data
}

export const getSleeperLeagues = async (data: SleeperRequest) => {
    if (!data.user_id || !data.year) {
        throw new Error("User ID and Year are required")
    }

    const response = await axiosInstance.get(`/api/sleeper/leagues/${data.user_id}/${data.year}`)

    return response.data
}