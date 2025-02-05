import { useState } from "react";
import { Form, Button } from "react-bootstrap";

interface SleeperFormProps {
    onBack: () => void
}

const SleeperForm: React.FC<SleeperFormProps> = ({ onBack }) => {
    const [username, setUsername] = useState("");

    const handleSubmit = () => {
        console.log("Sleeper Username Submitted:", username);
        // Send data to API here
    };

    return (
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
    );
};

export default SleeperForm;