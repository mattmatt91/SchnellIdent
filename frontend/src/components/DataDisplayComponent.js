import React from 'react';
import DataPlotComponent from './DataPlotComponent';
import DataTableComponent from './DataTableComponent';
import './ButtonBar.css';

function DataDisplayComponent({ data, params }) {
    return (
        <div className='data-display'>
            <p>TESTSWETSETSETSETSE</p>
            <p>TESTSWETSETSETSETSE</p>
            <p>TESTSWETSETSETSETSE</p>
            <p>TESTSWETSETSETSETSE</p>
            <p>TESTSWETSETSETSETSE</p>
            <p>TESTSWETSETSETSETSE</p>
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

