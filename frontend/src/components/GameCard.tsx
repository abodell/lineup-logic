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

const GameCard: React.FC<GameCardProps> = ({ homeTeam, awayTeam, homeScore, awayScore, date, gameType }) => {
    return (
        <Card className="mb-3 shadow-sm text-center mx-auto" style={{ width: '16rem' }}>
            <Card.Header className="bg-light py-2 bg-transparent border-0">
                <h6 className="mb-1">{gameType}</h6>
                <small className="text-muted">{date}</small>
            </Card.Header>
            <Card.Body className="py-3">
                <Row className="align-items-center g-5">
                    {/* Home Team Column */}
                    <Col xs={6} className="text-end">
                        <div className="d-flex flex-column align-items-end">
                            <div className="mb-2" style={{ height: '48px', display: 'flex', alignItems: 'center' }}>
                                <small className="fw-semibold text-end">{homeTeam}</small>
                            </div>
                            <span className="fs-5 fw-bold">{homeScore}</span>
                        </div>
                    </Col>
                    
                    {/* Away Team Column */}
                    <Col xs={6} className="text-start">
                        <div className="d-flex flex-column align-items-start">
                            <div className="mb-2" style={{ height: '48px', display: 'flex', alignItems: 'center' }}>
                                <small className="fw-semibold text-start">{awayTeam}</small>
                            </div>
                            <span className="fs-5 fw-bold">{awayScore}</span>
                        </div>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    )
}

export default GameCard