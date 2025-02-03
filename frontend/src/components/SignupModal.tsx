// src/components/SignupModal.tsx
import React from 'react';
import { Modal, Button, Form } from 'react-bootstrap';

interface SignupModalProps {
  show: boolean;
  handleClose: () => void;
}

const SignupModal: React.FC<SignupModalProps> = ({ show, handleClose }) => {
  return (
    <Modal show={show} onHide={handleClose} centered>
      <Modal.Header closeButton>
        <Modal.Title>Create Account</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Form.Group className="mb-3" controlId="signupFirstName">
            <Form.Label>First Name</Form.Label>
            <Form.Control type="text" placeholder="John" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="signupLastName">
            <Form.Label>Last Name</Form.Label>
            <Form.Control type="text" placeholder="Smith" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="signupEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="johnsmith@gmail.com" />
          </Form.Group>
          <Form.Group className="mb-3" controlId="signupPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Your Password" />
          </Form.Group>
        </Form>
      </Modal.Body>
      <Modal.Footer className="d-flex justify-content-center">
        <Button variant="primary" onClick={handleClose}>
          Create Account
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default SignupModal;