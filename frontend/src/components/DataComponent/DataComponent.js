import React, { useState, useEffect } from 'react';
import './DataComponent.css';
import DataDisplayComponent from '..//DataDisplayComponent/DataDisplayComponent';
import * as API from '../../service/api'

function PlotComponent() {
  const [ids, setIds] = useState([]);
  const [selectedId, setSelectedId] = useState('');
  const [data, setData] = useState(null);
  const [params, setParams] = useState(null);

  useEffect(() => {
    const fetchIds = async () => {
      try {
        const idList = await API.getAllIds();
        setIds(idList);
        
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
        // Await the async call to ensure the promise resolves
        const responseData = await API.getMeasurementById(selectedId);
        
        // Assuming the responseData is structured correctly
        if (responseData) {
          setData(responseData.data);  // Assuming responseData has a data property
          setParams(responseData.params); // Assuming responseData has a params property
        } else {
          console.error('Error fetching data: No response data');
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