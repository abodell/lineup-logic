import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import LandingPage from './pages/LandingPage'
import { AuthProvider } from './context/AuthContext'
import Leagues from './pages/Leagues'
import Betting from './pages/Betting'

function App() {

  return (
    <Router>
      <AuthProvider>
        <Layout>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/leagues" element={<Leagues />} />
            <Route path="/betting" element={<Betting />} />
          </Routes>
        </Layout>
      </AuthProvider>
    </Router>
  )
}

export default App
