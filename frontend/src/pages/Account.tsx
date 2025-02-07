import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card, Button, Spinner } from 'react-bootstrap'
import { useAuth } from '../context/AuthContext'
import { Link } from 'react-router-dom';
import ConnectLeagueModal from '../components/modals/ConnectLeagueModal';

interface League {
    id: string
    league_name: string
    league_details?: any
    created_at: string
}

const Account: React.FC = () => {
    const { user } = useAuth()
    const [leagues, setLeagues] = useState<League[]>([])
    const [loading, setLoading] = useState(false)
    const [showModal, setShowModal] = useState(false)

    return (
        <Container className="mt-5 pt-5">
            <h2 className="mb-4 text-center">Leagues</h2>
            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" />
                </div>
            ) : (
                <Row xs={1} sm={2} md={3} lg={4} className="g-4">
                    { /* Card for connecting a new league */ }
                    <Col>
                        <Card className="h-100 border-primary text-center" style={{ width: '18rem', minHeight: '10rem' }}>
                            <Card.Body className="d-flex flex-column justify-content-center align-items-center">
                                <Card.Title>Connect a New League</Card.Title>
                                <Button variant="outline-primary" onClick={() => setShowModal(true)}>
                                    Connect
                                </Button>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            )}
            { /* Modal Component */ }
            <ConnectLeagueModal show={showModal} handleClose={() => setShowModal(false)} />
        </Container>
    )
}

export default Account