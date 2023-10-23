// App.js
import './App.css';
import Header from './components/Header';
import ButtonBar from './components/ButtonBar';
import MeasureComponent from './components/MeasureComponent';
import PlotComponent from './components/DataComponent';
import React, { useState } from 'react';

function App() {
  const [activeComponent, setActiveComponent] = useState(null);

  return (
    <div className="app">
      <p>
        <Header className="header" />
      </p>
      <p>
        {activeComponent === 'measure' && <MeasureComponent className="measure" />}
        {activeComponent === 'plot' && <PlotComponent className="data" />}
      </p>
      <p>
        <ButtonBar setActiveComponent={setActiveComponent} className="footer" />
      </p>
    </div>
  );
}

export default App;
