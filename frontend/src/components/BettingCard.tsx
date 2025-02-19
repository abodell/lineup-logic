import React from 'react'
import { Card, Row, Col, Badge } from 'react-bootstrap'

interface BettingCardProps {
    homeTeam: string
    awayTeam: string
    homeSpread: number
    awaySpread: number
    total: number
    overOdds: number
    underOdds: number
    homeML: number
    awayML: number
    gameDate: string
    winningML?: string
    winningTotal?: string
    winningSpread?: string
}

const BettingCard: React.FC<BettingCardProps> = ({
    homeTeam,
    awayTeam,
    homeSpread,
    awaySpread,
    total,
    overOdds,
    underOdds,
    homeML,
    awayML,
    gameDate,
    winningML,
    winningTotal,
    winningSpread
}) => {
    // Function to style moneyline odds (positive for underdogs, negative for favorites)
    const formatOdds = (odds: number) => {
        return odds > 0 ? `+${odds}` : odds.toString()
    }


    return (
        <Card className="shadow-lg rounded-3 p-3 border-0" style={{ minWidth: "22rem", maxWidth: "30rem" }}>
            <Card.Header className="bg-dark text-white text-center">
                <h5 className="mb-0">{awayTeam} @ {homeTeam}</h5>
                <small>{gameDate}</small>
            </Card.Header>
            <Card.Body>
                <Row className="text-center">
                    <Col className="g-2">
                        <h6>Moneyline</h6>
                        <div>
                            <Badge bg={winningML === "Home ML" ? "success" : "secondary"}>{homeTeam} {formatOdds(homeML)}</Badge>
                        </div>
                        <div>
                            <Badge bg={winningML === "Away ML" ? "success" : "secondary"}>{awayTeam} {formatOdds(awayML)}</Badge>
                        </div>
                    </Col>
                    <Col className="g-2">
                        <h6>Spread</h6>
                        <div>
                            <Badge bg={winningSpread === "Away Cover" ? "success" : "secondary"}>{awayTeam} {awaySpread > 0 ? `+${awaySpread}` : awaySpread}</Badge>
                        </div>
                        <div>
                            <Badge bg={winningSpread === "Home Cover" ? "success" : "secondary"}>{homeTeam} {homeSpread > 0 ? `+${homeSpread}` : homeSpread}</Badge>
                        </div>
                    </Col>
                    <Col className="g-2">
                        <h6>Total</h6>
                        <div>
                            <Badge bg={winningTotal === "Over" ? "success" : "secondary"}>O {total} ({formatOdds(overOdds)})</Badge>
                        </div>
                        <div>
                            <Badge bg={winningTotal === "Under" ? "success" : "secondary"}>U {total} ({formatOdds(underOdds)})</Badge>
                        </div>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    )
}

export default BettingCard