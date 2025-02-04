import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import { AuthProvider } from './context/AuthContext'

function App() {

  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<LandingPage />} />
        </Routes>
      </AuthProvider>
    </Router>
  )
}

export default App
