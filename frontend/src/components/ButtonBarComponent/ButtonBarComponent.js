import { MEASURE, PLOT } from '../../App';
import './ButtonBarComponent.css';
import React from 'react';

function ButtonBar({ setActiveComponent }) {
  return (
    <div className="footer">
      <button className="button" onClick={() => setActiveComponent(MEASURE)}>
        Measure
      </button>
      <button className="button" onClick={() => setActiveComponent(PLOT)}>
        Data
      </button>
    </div>
  );
}

export default ButtonBar;
