// src/components/SignupModal.tsx
import React, { useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';
import { useAuth } from '../../context/AuthContext';

interface SignupModalProps {
  show: boolean;
  handleClose: () => void;
}

const SignupModal: React.FC<SignupModalProps> = ({ show, handleClose }) => {
  const { signUp } = useAuth()
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string| null>(null)

  const handleSignUp = async() => {
    setError(null)
    try {
      await signUp(email, password, firstName, lastName)
      handleClose()
    } catch (err) {
      setError('Error creating account. Please try again.')
      console.error(err)
    }
  }

  return (
    <Modal show={show} onHide={handleClose} centered>
      <Modal.Header closeButton>
        <Modal.Title>Create Account</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {error && <div className="text-danger mb-2">{error}</div>}
        <Form>
          <Form.Group className="mb-3" controlId="signupFirstName">
            <Form.Label>First Name</Form.Label>
            <Form.Control 
              type="text"
              placeholder="John" 
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
          </Form.Group>
          <Form.Group className="mb-3" controlId="signupLastName">
            <Form.Label>Last Name</Form.Label>
            <Form.Control 
              type="text"
              placeholder="Smith" 
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
          </Form.Group>
          <Form.Group className="mb-3" controlId="signupEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control 
              type="email"
              placeholder="johnsmith@gmail.com" 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </Form.Group>
          <Form.Group className="mb-3" controlId="signupPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control 
              type="password"
              placeholder="Your Password" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </Form.Group>
        </Form>
      </Modal.Body>
      <Modal.Footer className="d-flex justify-content-center">
        <Button variant="primary" onClick={handleSignUp}>
          Create Account
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default SignupModal;