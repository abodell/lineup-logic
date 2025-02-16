import React from 'react'
import Navigation from './Navigation'
import Footer from './Footer'

interface LayoutProps {
    children: React.ReactNode
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
    return (
        <div className="d-flex flex-column min-h-screen w-100">
            <Navigation />
            <main className="flex-grow-1">{children}</main>
            <Footer />
        </div>
    )
}

export default Layout