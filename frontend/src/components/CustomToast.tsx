import React from 'react'
import { Toast, ToastContainer } from 'react-bootstrap'

interface Props {
    show: boolean
    message: string
    onClose: () => void
}

const CustomToast: React.FC<Props> = ({ show, message, onClose }) => {
    return (
        <ToastContainer position="top-end" className="p-3">
            <Toast show={show} onClose={onClose} delay={3000} autohide>
                <Toast.Header>
                    <strong className="me-auto">Notification</strong>
                </Toast.Header>
                <Toast.Body>{message}</Toast.Body>
            </Toast>
        </ToastContainer>
    )
}

export default CustomToast
