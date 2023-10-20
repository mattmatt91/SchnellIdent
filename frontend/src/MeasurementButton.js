import React, { useState } from 'react';

function MeasurementButton() {
  const [measurementId, setMeasurementId] = useState(null);

  const startMeasurement = async () => {
    // Send a request to your backend endpoint
    try {
      const response = await fetch('http://backend/measurement');
      const data = await response.json();
      setMeasurementId(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <button onClick={startMeasurement}>Start Measurement</button>
      {measurementId && <p>Measurement ID: {measurementId}</p>}
    </div>
  );
}

export default MeasurementButton;
