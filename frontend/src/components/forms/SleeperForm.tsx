import { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { saveSleeperUser } from "../../api/sleeper";
import toast from "react-hot-toast";

interface SleeperFormProps {
    onBack: () => void
    onCloseModal: () => void
}

const SleeperForm: React.FC<SleeperFormProps> = ({ onBack, onCloseModal }) => {
    const [username, setUsername] = useState("");

    const handleSubmit = async () => {
        try {
            await saveSleeperUser({ username })
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
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Enter Sleeper Username"
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