import React from 'react';
import DataPlotComponent from './DataPlotComponent';
import DataTableComponent from './DataTableComponent';

function DataDisplayComponent({ data, params }) {
    return (
        <div>
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

