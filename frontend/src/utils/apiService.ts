import axios, { AxiosInstance } from 'axios'

const API_BASE_URL = "http://localhost:8000"

const axiosInstance: AxiosInstance = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true
})

export default axiosInstance