import React from 'react'
import { Container, Button } from 'react-bootstrap'
import '../styles/custom.css'

const HeroSection: React.FC = () => {
    return (
        <div className="hero-section d-flex align-items-center text-center text-white">
            <Container>
                <h1 className="display-4">Welcome to Lineup Logic</h1>
                <p className="lead">Play smarter, win bigger</p>
                <Button variant="primary" size="lg" href="/signup">
                    Get Started
                </Button>
            </Container>
        </div>
    )
}

export default HeroSection