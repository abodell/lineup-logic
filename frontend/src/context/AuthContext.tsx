import React, { createContext, useContext, useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login, logout, register, getCurrentUser } from '../api/auth'
import CustomToast from '../components/CustomToast'

export interface User {
    id: string
    email: string
    first_name?: string
    last_name?: string
}

interface AuthContextType {
    user: User | null
    loading: boolean
    signIn: (email: string, password: string) => Promise<void>
    signOut: () => Promise<void>
    signUp: (email: string, password: string, first_name: string, last_name: string) => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [user, setUser] = useState<User | null>(null)
    const [loading, setLoading] = useState(true)
    const [toastMessage, setToastMessage] = useState<string>('')
    const [showToast, setShowToast] = useState<boolean>(false)
    const navigate = useNavigate()

    useEffect( () => {
        const checkAuth = async () => {
            try {
                const currentUser = await getCurrentUser()
                setUser(currentUser)
            } catch (err) {
                setUser(null)
                console.error('Error fetching current user:', err)
            } finally {
                setLoading(false)
            }
        }
        checkAuth()
    }, [])

    const signIn = async (email: string, password: string) => {
        await login({ email, password })
        const currentUser = await getCurrentUser()
        setUser(currentUser)
        navigate('/')
    }

    const signUp = async (email: string, password: string, first_name: string, last_name: string) => {
        await register({ email, password, first_name, last_name })
        setToastMessage('Account created successfully! Please login.')
        setShowToast(true)
        setTimeout( () => navigate('/'), 3000)
    }

    const signOut = async () => {
        await logout()
        setUser(null)
        navigate('/')
    }

    return (
        <AuthContext.Provider value={{ user, loading, signIn, signOut, signUp }}>
            <CustomToast show={showToast} message={toastMessage} onClose={() => setShowToast(false)} />
            { children }
        </AuthContext.Provider>
    )
}

export const useAuth = (): AuthContextType => {
    const context = useContext(AuthContext)
    if (!context) throw new Error('useAuth must be used within AuthProvider')
    return context
}