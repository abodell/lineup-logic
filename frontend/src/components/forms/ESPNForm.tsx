import { useState } from "react";
import { Form, Button } from "react-bootstrap";

interface ESPNFormProps {
    onBack: () => void
}

const ESPNForm: React.FC<ESPNFormProps> = ({ onBack }) => {
    const [formData, setFormData] = useState({
        leagueId: "",
        year: "",
        swid: "",
        s2: ""
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = () => {
        console.log("ESPN Data Submitted:", formData);
        // Send data to API here
    };

    return (
        <Form>
            <Form.Group>
                <Form.Label>League ID</Form.Label>
                <Form.Control
                    type="text"
                    name="leagueId"
                    value={formData.leagueId}
                    onChange={handleChange}
                    placeholder="Enter League ID"
                />
            </Form.Group>
            <Form.Group>
                <Form.Label>Year</Form.Label>
                <Form.Control
                    type="number"
                    name="year"
                    value={formData.year}
                    onChange={handleChange}
                    placeholder="Enter Year"
                />
            </Form.Group>
            <Form.Group>
                <Form.Label>SWID</Form.Label>
                <Form.Control
                    type="text"
                    name="swid"
                    value={formData.swid}
                    onChange={handleChange}
                    placeholder="Enter SWID"
                />
            </Form.Group>
            <Form.Group>
                <Form.Label>S2</Form.Label>
                <Form.Control
                    type="text"
                    name="s2"
                    value={formData.s2}
                    onChange={handleChange}
                    placeholder="Enter S2"
                />
            </Form.Group>
            <p className="mt-2">
                <a href="https://example.com" target="_blank" rel="noopener noreferrer">
                    Where do I find this info?
                </a>
            </p>
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

export default ESPNForm;