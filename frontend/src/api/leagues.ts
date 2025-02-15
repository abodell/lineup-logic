import axiosInstance from "../utils/apiService";
import { LeaguesRequest } from "../types/Leagues";

export const getLeagues = async (data: LeaguesRequest) => {
    if (!data.user_id) {
        throw new Error("User ID required")
    }

    const response = await axiosInstance.get(`/api/leagues/${data.user_id}`)

    return response.data
}