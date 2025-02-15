import { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { saveESPNLeague } from "../../api/espn";
import toast from "react-hot-toast";

interface ESPNFormProps {
    onBack: () => void
    onCloseModal: () => void
}

const ESPNForm: React.FC<ESPNFormProps> = ({ onBack, onCloseModal }) => {
    const [formData, setFormData] = useState({
        league_id: "",
        year: Number(new Date().getFullYear()),
        swid: "",
        espn_s2: "",
        team_name: ""
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault()
        try {
            await saveESPNLeague({ ...formData })
            toast.success("ESPN league connected!")
    
            setTimeout(() => {
                onCloseModal()
                window.location.reload()
            }, 2000)
        } catch (err) {
            console.error("Error submitting ESPN form:", err)
        }
    };

    return (
        <Form>
            <Form.Group>
                <Form.Label>Team Name</Form.Label>
                <Form.Control
                    type="text"
                    name="team_name"
                    value={formData.team_name}
                    onChange={handleChange}
                    placeholder="Enter Team Name"
                />
            </Form.Group>
            <Form.Group>
                <Form.Label>League ID</Form.Label>
                <Form.Control
                    type="text"
                    name="league_id"
                    value={formData.league_id}
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
                    name="espn_s2"
                    value={formData.espn_s2}
                    onChange={handleChange}
                    placeholder="Enter S2"
                />
            </Form.Group>
            <p className="mt-2">
                <a href="https://github.com/cwendt94/espn-api/discussions/150" target="_blank" rel="noopener noreferrer">
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