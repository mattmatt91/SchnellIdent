import React, { useState, useEffect } from 'react';
import './DataComponent.css';
import DataDisplayComponent from '..//DataDisplayComponent/DataDisplayComponent';

function PlotComponent() {
  const [ids, setIds] = useState([]);
  const [selectedId, setSelectedId] = useState('');
  const [data, setData] = useState(null);
  const [params, setParams] = useState(null);

  useEffect(() => {
    const fetchIds = async () => {
      try {
        const localIpAddress = process.env.LOCAL_IP_ADDRESS || '192.168.1.30';
        const response = await fetch(`http://0.0.0.0:4000/get_all_ids`, {mode:'cors'});
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
  }, [ids]);

  const fetchData = async () => {
    if (selectedId) {
      try {
        const localIpAddress = process.env.LOCAL_IP_ADDRESS || '192.168.1.30';
        const response = await fetch(`http://0.0.0.0:4000/get_measurement/${selectedId}`, {mode:'cors'});
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
    <div className="data">
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
      <div>
        <DataDisplayComponent data={data} params={params} />
      </div>
    </div>
  );
}

export default PlotComponent;