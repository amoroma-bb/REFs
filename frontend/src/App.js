import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:5050/api/message")
      .then((response) => response.json())
      .then((data) => setMessage(data.message));
  }, []);

  return (
    <div className="App">
      <h1>React and Flask</h1>
      <p>Message from the backend: {message}</p>
    </div>
  );
}

export default App;
