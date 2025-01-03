import logo from './logo.svg';
import { useEffect, useState } from 'react';
import './App.css';
import { ping } from './services/api';

function App() {

  const [message, setMessage] = useState("")

  useEffect(() => {
    const fetchData = async () => {
      const data = await ping()
      setMessage(data.message)
    }
    fetchData()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and hello save to reload.
          backend says: {message}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
