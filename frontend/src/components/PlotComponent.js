import React, { useState, useEffect } from 'react';
import './PlotComponent.css';
import DataPlotComponent from './DataPlotComponent';

function PlotComponent() {
  const [ids, setIds] = useState([]);
  const [selectedId, setSelectedId] = useState('');
  const [data, setData] = useState([]); // Initialize data as an empty array

  useEffect(() => {
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

    fetchIds();
  }, []);

  const fetchData = async () => {
    if (selectedId) {
      try {
        const response = await fetch(`http://localhost:4000/get_measurement/${selectedId}`);
        if (response.ok) {
          const measurementData = await response.json();
          setData(measurementData);
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
      {data.length > 0 && <DataPlotComponent data={data} />}
    </div>
  );
}

export default PlotComponent;
