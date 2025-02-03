import React from 'react'
import { Container, Row, Col, Card } from 'react-bootstrap'

const Features: React.FC = () => {
    return (
        <Container className='my-5'>
            <h2 className="text-center mb-4">Our Features</h2>
            <Row>
                <Col md={4}>
                    <Card className="mb-4">
                        <Card.Body>
                            <Card.Title>Feature One</Card.Title>
                            <Card.Text>
                                A brief description
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Col>
                <Col md={4}>
                    <Card className="mb-4">
                        <Card.Body>
                            <Card.Title>Feature Two</Card.Title>
                            <Card.Text>
                                A brief description
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Col>
                <Col md={4}>
                    <Card className="mb-4">
                        <Card.Body>
                            <Card.Title>Feature Three</Card.Title>
                            <Card.Text>
                                A brief description
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    )
}

export default Features