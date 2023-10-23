import React, { useState } from 'react';
import { ClipLoader } from 'react-spinners';
import './MeasureComponent.css';
import DataDisplayComponent from './DataDisplayComponent';

function MeasureComponent() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [params, setParams] = useState(null);

  const handleRequest = async () => {
    setLoading(true);

    try {
      const response = await fetch('http://localhost:4000/measurement');
      const responseData = await response.json();

      const measurementData = responseData.data;
      const measurementParams = responseData.params;

      setData(measurementData);
      setParams(measurementParams);

      setLoading(false);
    } catch (error) {
      console.error('Error:', error);
      setLoading(false);
    }
  }

  return (
    <div className='measure'>
      {loading ? (
        <div className="loading-animation">
          <ClipLoader color={'red'} loading={loading} size={100} />
        </div>
      ) : data ? (
        <div className='canvas'>
          <div>
            <DataDisplayComponent className="data-display" data={data} params={params} />
          </div>
          <div>
            <button className="back-button" onClick={() => setData(null)}>
              Back to Measurement
            </button>
          </div>
        </div>
      ) : (
        <button className="start-button" onClick={handleRequest}>
          Start Measurement
        </button>
      )}
    </div>
  );
  
}

export default MeasureComponent;
