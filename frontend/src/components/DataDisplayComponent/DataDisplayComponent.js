import React from 'react';
import DataPlotComponent from '../PlotComponent/PlotComponent';
import DataTableComponent from '../TableComponent/TableComponent';
import './DataDisplayComponent.css';

function DataDisplayComponent({ data, params, selectedId, onDownloadMeasurement, onDeleteMeasurement }) {
  return (
    <div className='data-display'>
      {params && <DataTableComponent params={params} />}
      {data && <DataPlotComponent data={data} />}
      <div className="buttonbar-data-component">
        <button 
          className='button' 
          onClick={onDownloadMeasurement}
        >
          Download this Measurement
        </button>
        <button 
          className='button' 
          onClick={onDeleteMeasurement}
        >
          Delete this Measurement
        </button>
      </div>
    </div>
  );
}

export default DataDisplayComponent;
