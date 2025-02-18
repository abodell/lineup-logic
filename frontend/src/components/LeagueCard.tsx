import React from 'react'
import { Card, Col } from 'react-bootstrap'

interface LeagueCardProps {
    platform: 'espn' | 'sleeper'
    name: string
    teamName: string
    wins: number
    losses: number
    numTeams: number
}

const LeagueCard: React.FC<LeagueCardProps> = ({ platform, name, teamName, wins, losses, numTeams }) => {
    const logoSrc = platform === 'espn' ? '/espn.jpeg' : '/sleeper.jpeg'

    return (
        <Col className="d-flex justify-content-center">
            <Card className="h-100 shadow-lg rounded-3 border-0" style={{ minWidth: "20rem", maxWidth: "24rem" }}>
                <Card.Header className="d-flex align-items-center justify-content-center gap-3 bg-transparent">
                    <img src={logoSrc} alt={`${platform} Logo`} style={{ height: '40px', borderRadius: '10px' }} />
                    <h5 className="mb-0">{name}</h5>
                </Card.Header>
                <Card.Body className="text-center">
                    <div className="mb-2">
                        <strong>Owner:</strong> {teamName}
                    </div>
                    <div className="mb-2">
                        <strong>Record:</strong> {wins} - {losses}
                    </div>
                    <div className="mb-2">
                        <strong>Teams:</strong> {numTeams}
                    </div>
                </Card.Body>
            </Card>
        </Col>
    )
}

export default LeagueCard