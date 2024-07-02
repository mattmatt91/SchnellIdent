import React, { useState, useEffect } from 'react';
import './DataComponent.css';
import DataDisplayComponent from '../DataDisplayComponent/DataDisplayComponent';
import * as API from '../../service/api';

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
    if (!selectedId) {
      console.error('No ID selected');
      return;
    }
    try {
      const responseData = await API.getMeasurementById(selectedId);
      if (responseData) {
        setData(responseData.data);  // Assuming responseData has a data property
        setParams(responseData.params); // Assuming responseData has a params property
      } else {
        console.error('Error fetching data: No response data');
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleDownloadMeasurement = async () => {
    if (!selectedId) {
      console.error('No ID selected');
      return;
    }
    try {
      await API.downloadMeasurementById(selectedId);
    } catch (error) {
      console.error('Error downloading measurement:', error);
    }
  };

  const handleDeleteMeasurement = async () => {
    if (!selectedId) {
      console.error('No ID selected');
      return;
    }
    try {
      await API.deleteMeasurementById(selectedId);
    } catch (error) {
      console.error('Error deleting measurement:', error);
    }
  };

  return (
    <>
      <div className="buttonbar-data-component">
        <select className='button' value={selectedId} onChange={(e) => setSelectedId(e.target.value)}>
          <option value="">Select an ID</option>
          {ids.map((id) => (
            <option key={id} value={id}>
              {id}
            </option>
          ))}
        </select>
        <button className='button' onClick={fetchData}>Fetch Data</button>
      </div>
      <div className="data-display">
        <DataDisplayComponent 
          data={data} 
          params={params} 
          selectedId={selectedId} 
          onDownloadMeasurement={handleDownloadMeasurement} 
          onDeleteMeasurement={handleDeleteMeasurement} 
        />
      </div>
      <div className="buttonbar-data-component">
        <button className='button' onClick={API.downloadAllMeasurements}>Download all Measurements</button>
      </div>
    </>
  );
}

export default PlotComponent;
