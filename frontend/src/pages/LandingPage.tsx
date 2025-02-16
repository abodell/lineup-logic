import React, { useState, useEffect } from 'react'
import { Container } from 'react-bootstrap'
import HeroSection from '../components/HeroSection'
import CustomSlider from '../components/CustomSlider'
import { Game } from '../types/NFL'
import GameCard from '../components/GameCard'
import { getRecentGames } from '../api/nfl'

const LandingPage: React.FC = () => {
    const [recentGames, setRecentGames] = useState<Game[]>([])

    useEffect(() => {
        const fetchRecentGames = async () => {
            const response = await getRecentGames()
            setRecentGames(response)
        }
        fetchRecentGames()
    }, [])

    return (
        <Container fluid>
            {/*<CustomSlider>
                {recentGames?.map((game) => (
                    <GameCard  
                        key={game.gameid}
                        homeTeam={game.home_team.team_name}
                        awayTeam={game.away_team.team_name}
                        awayScore={game.total_away_points}
                        homeScore={game.total_home_points}
                        date={new Date(game.start_time).toLocaleDateString()}
                        gameType={game.game_type}
                    />
                ))}
            </CustomSlider>*/}
            <HeroSection />
        </Container>
    )
}

export default LandingPage