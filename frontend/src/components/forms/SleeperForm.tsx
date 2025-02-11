import { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { saveSleeperUser } from "../../api/sleeper";
import toast from "react-hot-toast";

interface SleeperFormProps {
    onBack: () => void
    onCloseModal: () => void
}

const SleeperForm: React.FC<SleeperFormProps> = ({ onBack, onCloseModal }) => {
    const [formData, setFormData] = useState({
        username: "",
        year: Number(new Date().getFullYear())
    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        try {
            await saveSleeperUser({ ...formData })
            toast.success("Sleeper account connected!")
    
            setTimeout(() => {
                onCloseModal()
                window.location.reload()
            }, 2000)
        } catch (err) {
            console.error("Error submitting Sleeper form:", err)
        }
    };

    return (
        <>
            <Form>
                <Form.Group>
                    <Form.Label>Sleeper Username</Form.Label>
                    <Form.Control
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        placeholder="Enter Sleeper Username"
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Year</Form.Label>
                    <Form.Control
                        type="number"
                        name="year"
                        value={formData.year}
                        onChange={handleChange}
                    />
                </Form.Group>
                <div className="mt-3 d-flex justify-content-between">
                    <Button variant="secondary" onClick={onBack}>
                        Back
                    </Button>
                    <Button variant="primary" onClick={handleSubmit}>
                        Submit
                    </Button>
                </div>
            </Form>
        </>
    );
};

export default SleeperForm;