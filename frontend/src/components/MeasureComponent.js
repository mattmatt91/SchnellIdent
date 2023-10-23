import React, { useState } from 'react';
import DataPlotComponent from './DataPlotComponent';
import { ClipLoader } from 'react-spinners';
import './MeasureComponent.css';

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
  };

  
  return (
    <div className="measure">
      {loading ? (
        <div className="loading-animation">
          <ClipLoader color={'red'} loading={loading} size={100} />
        </div>
      ) : data ? (
        <>
          <DataPlotComponent data={data} />
          <div className="params">
            <table>
              <thead></thead>
              <tbody>
                {Object.entries(params).map(([param, value]) => (
                  <tr key={param}>
                    <td>{param}</td>
                    <td style={{ color: param === 'explosive' ? (value ? 'red' : 'green') : 'white' }}>
                      {param === 'explosive' ? (value ? 'True' : 'False') : value}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <button className="back-button" onClick={() => setData(null)}>
            Back to Measurement
          </button>
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