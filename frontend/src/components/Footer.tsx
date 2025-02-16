import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

const Footer: React.FC = () => {
    return (
        <footer className="bg-light mt-auto">
            <Container>
                <Row className="justify-content-center">
                    <Col md={6}>
                        <p className="mb-0">&copy; {new Date().getFullYear()} Lineup Logic. All rights reserved.</p>
                    </Col>
                </Row>
            </Container>
        </footer>
    )
}

export default Footer