// MeasureComponent.js
import React from 'react';
//import './MeasureComponent.css';

function MeasureComponent() {
  const handleRequest = async () => {
    // Make a request to your backend here
    try {
      const response = await fetch('127.0.0.1:4000/measurement');
      const data = await response.json();
      console.log(data); // You can handle the response here
    } catch (error) {
      console.error('Error:', error); // Handle errors
    }
  };

  return (
    <div className="button-bar">
      <button className="button_green" onClick={handleRequest}>Start Measurement</button>
    </div>
  );
}

export default MeasureComponent;
