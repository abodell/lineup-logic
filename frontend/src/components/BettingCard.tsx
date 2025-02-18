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
    gameDate
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
                    <Col>
                        <h6>Spread</h6>
                        <Badge bg="secondary">{awayTeam} {awaySpread > 0 ? `+${awaySpread}` : awaySpread}</Badge>
                        <Badge bg="secondary">{homeTeam} {homeSpread > 0 ? `+${homeSpread}` : homeSpread}</Badge>
                    </Col>
                    <Col>
                        <h6>Total</h6>
                        <Badge bg="info">O {total} ({formatOdds(overOdds)})</Badge>
                        <Badge bg="info">U {total} ({formatOdds(underOdds)})</Badge>
                    </Col>
                    <Col>
                        <h6>Moneyline</h6>
                        <Badge bg={homeML < awayML ? "success" : "danger"}>{homeTeam} {formatOdds(homeML)}</Badge>
                        <Badge bg={awayML < homeML ? "success" : "danger"}>{awayTeam} {formatOdds(awayML)}</Badge>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    )
}

export default BettingCard