import React from 'react';
import './DataTableComponent.css'; //

function DataTableComponent({ params }) {
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
              <td style={{ color: param === 'explosive' ? (value ? 'red' : 'green') : 'white' }}>
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
