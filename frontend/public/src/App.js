import React from "react";
import UploadForm from "./components/UploadForm";
import "./styles.css";

function App() {
  return (
    <div className="app">
      <h1>🫁 Chest X-Ray Classifier</h1>
      <p>Upload a chest X-ray to predict if it’s Normal or Pneumonia</p>
      <UploadForm />
    </div>
  );
}

export default App;
