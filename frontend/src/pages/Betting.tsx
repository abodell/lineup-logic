import React, { useEffect, useState } from 'react'
import { Container, Row, Spinner, Col } from 'react-bootstrap'
import { getRecentBettingData } from '../api/betting'
import BettingCard from '../components/BettingCard'
import { BettingGame } from '../types/Betting'

const Betting: React.FC = () => {
    const [bettingData, setBettingData] = useState<BettingGame[]>([])
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        const fetchBettingData = async () => {
            setLoading(true)
            try {
                const data = await getRecentBettingData()
                setBettingData(data)
                console.log(data)
            } catch (err) {
                console.error("Error fetching betting data:", err)
            } finally {
                setLoading(false)
            }
        }
        fetchBettingData()
    }, [])

    return (
        <Container className="mt-4 pt-5 mb-4">
            <h2 className="text-center mb-4">Betting Odds</h2>

            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" />
                </div>
            ) : (
                <Row className="justify-content-center align-items-center g-4">
                    {bettingData.map((game, index) => (
                        <Col key={index} md={7} lg={5} className="g-4">
                            <BettingCard
                                homeTeam={game.game.home_team.team_abbr}
                                awayTeam={game.game.away_team.team_abbr}
                                homeSpread={game.home_spread}
                                awaySpread={game.away_spread}
                                total={game.total}
                                overOdds={game.over_line}
                                underOdds={game.under_line}
                                homeML={game.home_ml}
                                awayML={game.away_ml}
                                gameDate={new Date(game.game.start_time).toLocaleDateString()}
                                winningML={game.winning_ml_bet}
                                winningSpread={game.winning_spread_bet}
                                winningTotal={game.winning_total_bet}
                            />
                        </Col>
                    ))}
                </Row>
            )}
        </Container>
    )
}

export default Betting