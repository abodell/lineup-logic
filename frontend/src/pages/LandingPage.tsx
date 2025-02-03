import React from 'react'
import Navigation from '../components/Navigation'
import HeroSection from '../components/HeroSection'
import Features from '../components/Features'
import Footer from '../components/Footer'

const LandingPage: React.FC = () => {
    return (
        <>
            <Navigation />
            <HeroSection />
            <Features />
            <Footer />
        </>
    )
}

export default LandingPage