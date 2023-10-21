import React, { useState } from 'react';
import DataPlotComponent from './DataPlotComponent';
import { ClipLoader } from 'react-spinners'; // Import the ClipLoader spinner
import './MeasureComponent.css';

function MeasureComponent() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [params, setParams] = useState(null);

  const handleRequest = async () => {
    setLoading(true); // Show loading animation

    try {
      const response = await fetch('http://localhost:4000/measurement');
      const responseData = await response.json();

      const measurementData = responseData.data;
      const measurementParams = responseData.params;

      setData(measurementData);
      setParams(measurementParams);

      setLoading(false); // Hide loading animation when data is received
    } catch (error) {
      console.error('Error:', error);
      setLoading(false); // Hide loading animation in case of an error
    }
  };

  return (
    <div className="measure">
      {loading ? (
        <div className="loading-animation">
          <ClipLoader color={'red'} loading={loading} size={100} /> {/* Use ClipLoader */}
        </div>
      ) : data ? (
        <>
          <DataPlotComponent data={data} />
          <button className="back-button" onClick={() => setData(null)}>
            Back to Measurement
          </button>

          <div className="params">
            <p>Explosive: {params.explosive ? <span style={{ color: 'red' }}>True</span> : <span style={{ color: 'green' }}>False</span>}</p>
            {/* Add more parameter display here */}
          </div>
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
