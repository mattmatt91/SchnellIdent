// ButtonBar.js
import React from 'react';

function ButtonBar({ setActiveComponent }) {
  return (
    <div className="button-bar">
      <button className="button_red" onClick={() => setActiveComponent('measure')}>Measure</button>
      <button className="button_grey" onClick={() => setActiveComponent('plot')}>Plot</button>
    </div>
  );
}

export default ButtonBar;
