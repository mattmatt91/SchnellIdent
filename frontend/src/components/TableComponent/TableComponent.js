import React from 'react';
import './TableComponent.css'; //

function DataTableComponent({ params }) {
  console.log(params)
  return (
    <div className="params">
      <table>
        <thead>
          {/* Table header */}
          <tr>
            <th>Parameter</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(params).map(([param, value]) => (
            <tr key={param}>
              <td>{param}</td>
              <td style={{ backgroundColor: param === 'explosive' ? (value ? 'red' : 'green') : 'black' }}>
                {param === 'explosive' ? (value ? 'True' : 'False') : value}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DataTableComponent;
