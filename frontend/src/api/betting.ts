import axiosInstance from "../utils/apiService";

export const getRecentBettingData = async () => {
    try {
        const response = await axiosInstance.get('/api/betting/recent')
        return response.data
    } catch (err) {
        console.error("Error fetching betting data:", err)
    }
}