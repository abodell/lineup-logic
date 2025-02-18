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
        <Card className="h-80 border-0" style={{ width: '100%' }}>
            <Card.Header className="bg-transparent border-dark text-center">
                <div className="d-flex flex-column" style={{ minHeight: '65px' }}>
                    <h6 className="mb-1">{gameType}</h6>
                    <small className="text-muted">{date}</small>
                </div>
            </Card.Header>
            <Card.Body>
                <Row className="align-items-center justify-content-center">
                    <Col xs={5} className="text-align">
                        <div style={{ minHeight: '20px' }}>
                            <small className="fw-semibold">{homeTeam}</small>
                        </div>
                        <span className="fs-5 fw-bold">{homeScore}</span>
                    </Col>
                    <Col xs={5} className="text-align">
                        <div style={{ minHeight: '20px' }}>
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