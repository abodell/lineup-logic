import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

const Footer: React.FC = () => {
    return (
        <footer className="bg-light py-4 mt-auto">
            <Container>
                <Row>
                    <Col md={6}>
                        <p className="mb-0">&copy; {new Date().getFullYear()} Lineup Logic. All rights reserved.</p>
                    </Col>
                    <Col md={6} className="text-md-end">
                        <a href="/privacy" className="me-3">Privacy Policy</a>
                        <a href="/terms">Terms of Service</a>
                    </Col>
                </Row>
            </Container>
        </footer>
    )
}

export default Footer