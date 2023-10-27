import './App.css';
// App.js


import Header from './components/HeaderComponent/HeaderComponent';
import ButtonBar from './components/ButtonBarComponent/ButtonBarComponent';
import MeasureComponent from './components//MeasureComponent/MeasureComponent';
import PlotComponent from './components/DataComponent/DataComponent';
import React, { useEffect, useState } from 'react';

export const MEASURE ="measure"

export const PLOT ="plot"


function App() {
  const [activeComponent, setActiveComponent] = useState(null);

  return (
    <div className="app">

      <Header className="header" />

      {activeComponent === PLOT && <PlotComponent className="main" />}
      {activeComponent === MEASURE && <MeasureComponent className="main" />}

      <ButtonBar setActiveComponent={setActiveComponent} className="footer" />

    </div>
  );
}

export default App;
