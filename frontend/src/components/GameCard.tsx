import React from 'react'
import { Card, Row, Col } from 'react-bootstrap'

interface GameCardProps {
    homeTeam: string
    awayTeam: string
    homeScore: number
    awayScore: number
    date: string
    gameType: string
}

const GameCard: React.FC<GameCardProps> = ({ ...props }) => {
    return (
        <Card className="mb-4">
            <Card.Header>
                <Row>
                    <Col>
                        <h5>{props.gameType}</h5>
                        <p>{props.date}</p>
                    </Col>
                </Row>
            </Card.Header>
            <Card.Body>
                <Row>
                    <Col xs={6}>
                        <h6>{props.homeTeam}</h6>
                        <p>Score: {props.homeScore}</p>
                    </Col>
                    <Col xs={6}>
                        <h6>{props.awayTeam}</h6>
                        <p>{props.awayScore}</p>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    )
}

export default GameCard