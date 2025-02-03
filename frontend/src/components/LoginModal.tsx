import React from 'react'
import { Modal, Button, Form } from 'react-bootstrap'

interface LoginModalProps {
    show: boolean
    handleClose: () => void
}

const LoginModal: React.FC<LoginModalProps> = ({ show, handleClose }) => {
    return (
        <Modal show={show} onHide={handleClose} centered>
            <Modal.Header closeButton>
                <Modal.Title>Login</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group className="mb-3" controlId="loginEmail">
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control type="email" placeholder="johnsmith@gmail.com" />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="loginPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Your Password"/>
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer className="d-flex justify-content-center">
                <Button variant="primary" onClick={handleClose}>
                    Login
                </Button>
            </Modal.Footer>
        </Modal>
    )
}

export default LoginModal