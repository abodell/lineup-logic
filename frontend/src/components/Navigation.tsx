// src/components/Navigation.tsx
import React, { useState } from 'react';
import { Navbar, Nav, Container, Button, Dropdown } from 'react-bootstrap';
import { useAuth } from '../context/AuthContext'
import { Link } from 'react-router-dom';
import LoginModal from './LoginModal';
import SignupModal from './SignupModal';
import { FaRegUser } from 'react-icons/fa'

const Navigation: React.FC = () => {
  // State to control modal visibility
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);
  const { user, signOut } = useAuth()

  return (
    <>
      <Navbar bg="light" expand="lg" fixed="top" className="w-100 shadow">
        <Container>
          <Navbar.Brand as={Link} to='/'>Lineup Logic</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto align-items-center">
              <Nav.Link as={Link} to="/features">Features</Nav.Link>
              <Nav.Link as={Link} to="/pricing">Pricing</Nav.Link>
              <Nav.Link as={Link} to="/about">About</Nav.Link>
              <Nav.Link as={Link} to="/contact">Contact</Nav.Link>
              { /* If user is not logged in, show login and create account buttons */ }
              {!user && (
                <>
                  <Button variant="outline-primary" onClick={() => setShowLogin(true)} className="ms-2">
                    Login
                  </Button>
                  <Button variant="primary" onClick={() => setShowSignup(true)} className="ms-2">
                    Create Account
                  </Button>
                </>
              )}

              {/* If user is logged in, show dropdown to sign out and view account */ }
              {user && (
                <Dropdown align="end" className="ms-2">
                  <Dropdown.Toggle
                    variant="outline-secondary"
                    id="dropdown-user"
                    className="d-flex align-items-center"
                  >
                    <FaRegUser size={20} />
                  </Dropdown.Toggle>
                  <Dropdown.Menu>
                    <Dropdown.Item as={Link} to="/account">
                      View Account
                    </Dropdown.Item>
                    <Dropdown.Item onClick={signOut}>
                      Sign Out
                    </Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
              )}
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      {/* Login and Signup Modals */}
      <LoginModal show={showLogin} handleClose={() => setShowLogin(false)} />
      <SignupModal show={showSignup} handleClose={() => setShowSignup(false)} />
    </>
  );
};

export default Navigation;