import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card, Button, Spinner } from 'react-bootstrap'
import { useAuth } from '../context/AuthContext'
import ConnectLeagueModal from '../components/modals/ConnectLeagueModal';
import { getSleeperLeagues } from '../api/sleeper';
import { useSleeperInfo } from '../hooks/useSleeperInfo';

interface League {
    name: string
    num_teams: number
    wins: number
    losses: number
    team_name: string
}

const Account: React.FC = () => {
    const { user } = useAuth()
    const [leagues, setLeagues] = useState<League[]>([])
    const { info } = useSleeperInfo(user?.id || "")
    const [showModal, setShowModal] = useState(false)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const fetchLeagues = async () => {
            if (!user || !info || info.length == 0) {
                setLoading(false)
                return
            }

            try {
                const leaguePromises = info.map((leagueInfo: { sleeper_user_id: string; year: number }) => {
                    return getSleeperLeagues({user_id: leagueInfo.sleeper_user_id, year: leagueInfo.year })
                })
                
                const results = await Promise.all(leaguePromises)
                setLeagues(results[0])
            } catch (err) {
                console.error("Error fetching leagues:", err)
            } finally {
                setLoading(false)
            }
        }
        fetchLeagues()
    }, [user, info])

    return (
        <Container className="mt-3 pt-5">
            <h2 className="mb-4 text-center">Leagues</h2>
            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" />
                </div>
            ) : (
                <>
                <Row className="justify-content-center mb-4">
                    { /* Card for connecting a new league */ }
                    <Col className="d-flex justify-content-center">
                        <Card className="h-100 border-primary text-center">
                            <Card.Body className="d-flex flex-column justify-content-center align-items-center">
                                <Card.Title>Connect a New League</Card.Title>
                                <Button variant="outline-primary" onClick={() => setShowModal(true)}>
                                    Connect
                                </Button>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                    { /* Render a card for each connected league */ }
                <Row className="g-5 justify-content-center">
                    {leagues.map((league, index) => (
                        <Col key={index} className="d-flex justify-content-center">
                            <Card className="h-100" style={{minWidth: "18rem"}}>
                                <Card.Header className="d-flex align-items-center justify-content-center gap-3 bg-white">
                                    <img
                                        src="/sleeper.jpeg"
                                        alt="Sleeper Logo"
                                        style={{height: '35px', marginRight: '8px', borderRadius: '10px'}}
                                    />
                                    <h6>{league.name}</h6>
                                </Card.Header>
                                <Card.Body>
                                    <div className="mb-2">
                                        <strong>Record:</strong> {league.wins} - {league.losses}
                                    </div>
                                    <div className="mb-2">
                                        <strong>Teams:</strong>{league.num_teams}
                                    </div>
                                    <div>
                                        <strong>Owner:</strong> {league.team_name}
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            </>
            )}
            { /* Modal Component */ }
            <ConnectLeagueModal show={showModal} handleClose={() => setShowModal(false)} />
        </Container>
    )
}

export default Account