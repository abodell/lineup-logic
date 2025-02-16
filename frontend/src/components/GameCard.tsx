import React from 'react';
import { Card, Row, Col } from 'react-bootstrap';

interface GameCardProps {
    homeTeam: string;
    awayTeam: string;
    homeScore: number;
    awayScore: number;
    date: string;
    gameType: string;
}

const GameCard: React.FC<GameCardProps> = ({ homeTeam, awayTeam, homeScore, awayScore, date, gameType }) => {
    return (
        <Card className="h-100 shadow-sm" style={{ width: '100%' }}>
            <Card.Header className="bg-transparent border-0 py-2 text-center">
                <div className="d-flex flex-column" style={{ minHeight: '70px' }}>
                    <h6 className="mb-1">{gameType}</h6>
                    <small className="text-muted">{date}</small>
                </div>
            </Card.Header>
            <Card.Body className="py-2">
                <Row className="align-items-center justify-content-center">
                    <Col xs={5} className="text-align">
                        <div className="mb-2" style={{ minHeight: '40px' }}>
                            <small className="fw-semibold">{homeTeam}</small>
                        </div>
                        <span className="fs-5 fw-bold">{homeScore}</span>
                    </Col>
                    <Col xs={5} className="text-align">
                        <div className="mb-2" style={{ minHeight: '40px' }}>
                            <small className="fw-semibold">{awayTeam}</small>
                        </div>
                        <span className="fs-5 fw-bold">{awayScore}</span>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    );
};

export default GameCard;