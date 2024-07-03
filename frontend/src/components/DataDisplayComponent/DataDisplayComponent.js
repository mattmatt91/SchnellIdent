import React from 'react';
import DataPlotComponent from '../PlotComponent/PlotComponent';
import DataTableComponent from '../TableComponent/TableComponent';
import './DataDisplayComponent.css';

function DataDisplayComponent({ data, params, selectedId}) {
  return (
    <div className='data-display'>
      {params && <DataTableComponent params={params} />}
      {data && <DataPlotComponent data={data} />}
  
    </div>
  );
}

export default DataDisplayComponent;
