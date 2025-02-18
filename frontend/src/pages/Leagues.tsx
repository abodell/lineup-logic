import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card, Button, Spinner } from 'react-bootstrap'
import { useAuth } from '../context/AuthContext'
import ConnectLeagueModal from '../components/modals/ConnectLeagueModal'
import { getLeagues } from '../api/leagues'
import { League } from '../types/Leagues'
import LeagueCard from '../components/LeagueCard'

const Leagues: React.FC = () => {
    const { user } = useAuth()
    const [leagues, setLeagues] = useState<League | null>(null)
    const [showModal, setShowModal] = useState(false)
    const [loading, setLoading] = useState(false)

    useEffect(() => {
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

            {loading ? (
                <div className="text-center">
                    <Spinner animation="border" />
                </div>
            ) : (
                <Row className="g-4 justify-content-center">
                    {leagues?.espn?.map((league, index) => (
                        <LeagueCard
                            key={`espn-${index}`}
                            platform="espn"
                            name={league.name}
                            teamName={league.team_name}
                            wins={league.wins}
                            losses={league.losses}
                            numTeams={league.num_teams}
                        />
                    ))}
                    {leagues?.sleeper?.map((league, index) => (
                        <LeagueCard
                            key={`sleeper-${index}`}
                            platform="sleeper"
                            name={league.name}
                            teamName={league.team_name}
                            wins={league.wins}
                            losses={league.losses}
                            numTeams={league.num_teams}
                        />
                    ))}
                </Row>
            )}

            <ConnectLeagueModal show={showModal} handleClose={() => setShowModal(false)} />
        </Container>
    )
}

export default Leagues