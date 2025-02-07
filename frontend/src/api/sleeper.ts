import axiosInstance from "../utils/apiService";
import { SleeperRequest } from "../types/Sleeper";

export const saveSleeperUser = async (data: SleeperRequest) => {
    if (!data.username) {
        throw new Error('Username is required')
    }
    
    const response = await axiosInstance.post(`/api/sleeper/user?username=${data.username}`)
    return response.data
}