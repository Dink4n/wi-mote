import React from "react";
import "./App.css";
import { Container } from "semantic-ui-react";
import { Player } from "./components/Player";
import { Utilities } from "./components/Utilities";
import { Volume } from "./components/Volume";

function App() {
    return (
        <div className="App">
            <Container style={{ marginTop: 40 }}>
                <Utilities />
                <Player />
                <Volume />
            </Container>
        </div>
    );
}

export default App;
