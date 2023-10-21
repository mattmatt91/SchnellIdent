import React, { useState, useEffect } from 'react';
import './PlotComponent.css';
import DataPlotComponent from './DataPlotComponent';

function PlotComponent() {
  const [ids, setIds] = useState([]); // Initialize ids as an empty array
  const [selectedId, setSelectedId] = useState('');
  const [data, setData] = useState(null); // Initialize data as null
  const [params, setParams] = useState(null); // Initialize parameters as null

  useEffect(() => {
    // Fetch IDs only once on component mount
    const fetchIds = async () => {
      try {
        const response = await fetch('http://localhost:4000/get_all_ids');
        if (response.ok) {
          const idList = await response.json();
          setIds(idList);
        } else {
          console.error('Error fetching IDs:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching IDs:', error);
      }
    };

    if (ids.length === 0) {
      fetchIds();
    }
  }, [ids]); // This ensures that fetchIds is only called once

  const fetchData = async () => {
    if (selectedId) {
      try {
        const response = await fetch(`http://localhost:4000/get_measurement/${selectedId}`);
        if (response.ok) {
          const responseData = await response.json();
          const measurementData = responseData.data;
          const measurementParams = responseData.params;

          setData(measurementData);
          setParams(measurementParams);
        } else {
          console.error('Error fetching data:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  };

  return (
    <div className="plot-component">
      <div>
        <select value={selectedId} onChange={(e) => setSelectedId(e.target.value)}>
          <option value="">Select an ID</option>
          {ids.map((id) => (
            <option key={id} value={id}>
              {id}
            </option>
          ))}
        </select>
        <button onClick={fetchData}>Fetch Data</button>
      </div>
      {data && (
        <DataPlotComponent data={data} />
      )}
      {params && (
        <div className="params">
          <p>Explosive: {params.explosive ? <span style={{ color: 'red' }}>True</span> : <span style={{ color: 'green' }}>False</span>}</p>
          {/* Add more parameter display here */}
        </div>
      )}
    </div>
  );
}

export default PlotComponent;
