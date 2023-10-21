import React, { useState } from 'react';
import DataPlotComponent from './DataPlotComponent'; // Import the DataPlotComponent
import './MeasureComponent.css';

function MeasureComponent() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null); // To store the measurement data
  const [params, setParams] = useState(null); // To store the measurement parameters

  const handleRequest = async () => {
    // Show loading animation
    setLoading(true);

    try {
      const response = await fetch('http://localhost:4000/measurement');
      const responseData = await response.json();

      const measurementData = responseData.data;
      const measurementParams = responseData.params;
      // Store the measurement data and parameters
      setData(measurementData);
      setParams(measurementParams);

      // Hide loading animation when data is received
      setLoading(false);
    } catch (error) {
      console.error('Error:', error); // Handle errors

      // Hide loading animation in case of an error
      setLoading(false);
    }
  };



  return (
    <div className="measure">
      {loading ? (
        <div className="loading-animation">Measuring...</div>
      ) : data ? (
        <>
          <DataPlotComponent data={data} />
          <button className="back-button" onClick={() => setData(null)}>
            Back to Measurement
          </button>
         
            <p>Explosive: {params.explosive ? <span style={{ color: 'red' }}>True</span> : <span style={{ color: 'green' }}>False</span>}</p>
             

        </>
      ) : (
        <button className="start-button" onClick={handleRequest}>
          Start Measurement
        </button>
      )}
    </div>
  );
}

export default MeasureComponent;
