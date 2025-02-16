import axiosInstance from "../utils/apiService";

export const getRecentGames = async () => {
    try {
        const response = await axiosInstance.get('/api/nfl/recent-games')
        return response.data
    } catch(err) {
        console.error("Error fetching recent games:", err)
    }
}