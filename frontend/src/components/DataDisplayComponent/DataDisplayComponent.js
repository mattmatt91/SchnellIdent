import React from 'react';
import DataPlotComponent from '..//PlotComponent/PlotComponent';
import DataTableComponent from '..//TableComponent/TableComponent';
import './DataDisplayComponent.css';

function DataDisplayComponent({ data, params }) {
    return (
        <div className='data-display'>
            {data && (
                <DataPlotComponent data={data} />
            )}
            {params && (
                <DataTableComponent params={params} />
            )}
        </div>
    );
}
export default DataDisplayComponent;

