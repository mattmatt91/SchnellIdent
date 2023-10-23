import React from 'react';

function DataDisplayComponent({ data, params }) {
  return (
    <div className="data-display">
      <div className="data-plot">
        {data && /* Render your Plot component here */}
      </div>
      <div className="data-table">
        {params && (
          <table>
            <thead>
              {/* Table header */}
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
        )}
      </div>
    </div>
  );
}

export default DataDisplayComponent;
