import axiosInstance from "../utils/apiService";
import { AuthRequest } from "../types/Auth";

export const register = async (data: AuthRequest) => {
    const response = await axiosInstance.post('/auth/register', data)
    return response.data
}

export const login = async (data: AuthRequest) => {
    const response = await axiosInstance.post('/auth/login', data)
    return response.data
}

export const logout = async () => {
    const response = await axiosInstance.post('/auth/logout')
    return response.data
}

export const getCurrentUser = async () => {
    const response = await axiosInstance.get('/auth/current-user')
    return response.data
}