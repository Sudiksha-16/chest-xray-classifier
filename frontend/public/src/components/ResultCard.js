import React from "react";

const ResultCard = ({ result }) => {
  return (
    <div className="result-card">
      <h3>Prediction: {result.prediction}</h3>
      <p>Confidence:</p>
      <ul>
        <li>Normal: {(result.probabilities[0] * 100).toFixed(2)}%</li>
        <li>Pneumonia: {(result.probabilities[1] * 100).toFixed(2)}%</li>
      </ul>
    </div>
  );
};

export default ResultCard;
