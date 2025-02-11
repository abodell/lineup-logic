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