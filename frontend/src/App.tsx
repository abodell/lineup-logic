import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import LandingPage from './pages/LandingPage'
import { AuthProvider } from './context/AuthContext'
import Account from './pages/Account'

function App() {

  return (
    <Router>
      <AuthProvider>
        <Layout>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/account" element={<Account />} />
          </Routes>
        </Layout>
      </AuthProvider>
    </Router>
  )
}

export default App
