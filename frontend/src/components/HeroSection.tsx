import React from 'react'
import { Container } from 'react-bootstrap'
import '../styles/custom.css'

const HeroSection: React.FC = () => {
    return (
        <div className="hero-section d-flex align-items-center text-center text-white">
            <Container>
                <h1 className="display-4 text-primary">Welcome to Lineup Logic</h1>
                <p className="lead text-secondary">Play smarter, win bigger</p>
            </Container>
        </div>
    )
}

export default HeroSection