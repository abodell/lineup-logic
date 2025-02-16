import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card, Button, Spinner } from 'react-bootstrap'
import { useAuth } from '../context/AuthContext'
import ConnectLeagueModal from '../components/modals/ConnectLeagueModal';
import { getLeagues } from '../api/leagues';
import { League } from '../types/Leagues';


const Account: React.FC = () => {
    const { user } = useAuth()
    const [leagues, setLeagues] = useState<League | null>(null)
    const [showModal, setShowModal] = useState(false)
    const [loading, setLoading] = useState(false)

    useEffect( () => {
        const fetchLeagues = async () => {
            setLoading(true)
            try {
                const res = await getLeagues({ user_id: user?.id })
                setLeagues(res)
            } catch (err) {
                console.error("Error fetching leagues:", err)
            } finally {
                setLoading(false)
            }
        }
        
        if (user?.id) {
            fetchLeagues()
        }
    }, [user])

    console.log(leagues?.sleeper)

    return (
        <Container className="mt-4 pt-5">
            <h2 className="mb-4 text-center">Leagues</h2>

            <Row className="justify-content-center mb-4">
                <Col className="d-flex justify-content-center">
                    <Card className="h-100 border-primary text-center shadow-lg rounded-3" style={{ minWidth: "20rem" }}>
                        <Card.Body className="d-flex flex-column justify-content-center align-items-center">
                            <Card.Title className="mb-3">Connect a New League</Card.Title>
                            <Button variant="outline-primary" size="lg" onClick={() => setShowModal(true)}>
                                Connect
                            </Button>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>

            {/* Show spinner while league cards are loading */}
            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" />
                </div>
            ) : (
                <Row className="g-4 justify-content-center">
                    { /* Eventually need to make the cards a componenet */ }
                    {leagues?.espn?.map((league, index) => (
                        <Col key={`espn-${index}`} className="d-flex justify-content-center">
                            <Card className="h-100 shadow-lg rounded-3 border-0" style={{ minWidth: "20rem", maxWidth: "24rem" }}>
                                <Card.Header className="d-flex align-items-center justify-content-center gap-3 bg-transparent">
                                    <img
                                        src="/espn.jpeg"
                                        alt="ESPN Logo"
                                        style={{ height: '40px', borderRadius: '10px' }}
                                    />
                                    <h5 className="mb-0">{league.name}</h5>
                                </Card.Header>
                                <Card.Body className="text-center">
                                    <div className="mb-2">
                                        <strong>Owner:</strong> {league.team_name}
                                    </div>
                                    <div className="mb-2">
                                        <strong>Record:</strong> {league.wins} - {league.losses}
                                    </div>
                                    <div className="mb-2">
                                        <strong>Teams:</strong> {league.num_teams}
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                    {leagues?.sleeper?.map((league, index) => (
                        <Col key={`sleeper-${index}`} className="d-flex justify-content-center">
                            <Card className="h-100 shadow-lg rounded-3 border-0" style={{ minWidth: "20rem", maxWidth: "24rem" }}>
                                <Card.Header className="d-flex align-items-center justify-content-center gap-3 bg-transparent">
                                    <img
                                        src="/sleeper.jpeg"
                                        alt="Sleeper Logo"
                                        style={{ height: '40px', borderRadius: '10px' }}
                                    />
                                    <h5 className="mb-0">{league.name}</h5>
                                </Card.Header>
                                <Card.Body className="text-center">
                                    <div className="mb-2">
                                        <strong>Owner:</strong> {league.team_name}
                                    </div>
                                    <div className="mb-2">
                                        <strong>Record:</strong> {league.wins} - {league.losses}
                                    </div>
                                    <div className="mb-2">
                                        <strong>Teams:</strong> {league.num_teams}
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            )}

            {/* Modal Component */}
            <ConnectLeagueModal show={showModal} handleClose={() => setShowModal(false)} />
        </Container>
    );
};

export default Account