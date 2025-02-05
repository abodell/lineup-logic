import { useState } from "react";
import { Modal, Button } from "react-bootstrap";
import SleeperForm from "./forms/SleeperForm";
import ESPNForm from "./forms/ESPNForm";

interface ConnectLeagueModalProps {
    show: boolean
    handleClose: () => void
}

const ConnectLeagueModal: React.FC<ConnectLeagueModalProps> = ({ show, handleClose }) => {
    const [selectedPlatform, setSelectedPlatform] = useState<"main" | "sleeper" | "espn">("main");

    return (
        <Modal show={show} onHide={handleClose} centered>
            <Modal.Header closeButton>
                <Modal.Title>
                    {selectedPlatform === "main"
                        ? "Connect a Fantasy League"
                        : selectedPlatform === "sleeper"
                        ? "Connect Sleeper League"
                        : "Connect ESPN League"}
                </Modal.Title>
            </Modal.Header>

            <Modal.Body>
                {selectedPlatform === "main" && (
                    <div className="d-flex flex-column align-items-center">
                        <Button className="mb-3 w-100" variant="primary" onClick={() => setSelectedPlatform("sleeper")}>
                            Connect Sleeper
                        </Button>
                        <Button className="w-100" variant="danger" onClick={() => setSelectedPlatform("espn")}>
                            Connect ESPN
                        </Button>
                    </div>
                )}
                {selectedPlatform === "sleeper" && <SleeperForm onBack={() => setSelectedPlatform("main")} />}
                {selectedPlatform === "espn" && <ESPNForm onBack={() => setSelectedPlatform("main")} />}
            </Modal.Body>
        </Modal>
    );
};

export default ConnectLeagueModal;