import { useState, useEffect} from 'react'
import { getSleeperInfo } from '../api/sleeper'

export const useSleeperInfo = (userId: string) => {
    const [info, setInfo] = useState<any[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        const fetchLeagues = async () => {
            try {
                const res = await getSleeperInfo({user_id: userId})
                setInfo(res)
            } catch (err: any) {
                setError(err.message)
            } finally {
                setLoading(false)
            }
        }

        if (userId) {
            fetchLeagues()
        }
    }, [userId])

    return { info, loading, error }
}