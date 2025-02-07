import React, { useState } from 'react'
import { Modal, Button, Form } from 'react-bootstrap'
import { useAuth } from '../../context/AuthContext'

interface LoginModalProps {
    show: boolean
    handleClose: () => void
}

const LoginModal: React.FC<LoginModalProps> = ({ show, handleClose }) => {
    const { signIn } = useAuth()
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState<string | null>(null)

    const handleLogin = async () => {
        setError(null)
        try {
            await signIn(email, password)
            handleClose()
        } catch (err) {
            setError('Invalid email or password')
            console.error(err)
        }
    }

    return (
        <Modal show={show} onHide={handleClose} centered>
            <Modal.Header closeButton>
                <Modal.Title>Login</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                {error && <div className="text-dange mb-2">{error}</div>}
                <Form>
                    <Form.Group className="mb-3" controlId="loginEmail">
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control 
                            type="email"
                            placeholder="johnsmith@gmail.com" 
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="loginPassword">
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
                <Button variant="primary" onClick={handleLogin}>
                    Login
                </Button>
            </Modal.Footer>
        </Modal>
    )
}

export default LoginModal