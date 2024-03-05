// App.js

import React, { useState } from 'react';
import './App.css';
import Header from './components/HeaderComponent/HeaderComponent';
import ButtonBar from './components/ButtonBarComponent/ButtonBarComponent';
import MeasureComponent from './components/MeasureComponent/MeasureComponent';
import PlotComponent from './components/DataComponent/DataComponent';

export const MEASURE = "measure";
export const PLOT = "plot";

function App() {
  const [activeComponent, setActiveComponent] = useState(null);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch((err) => {
        console.error(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  };

  return (
    <div className="app">
      <Header className="header" toggleFullscreen={toggleFullscreen} />
      <div className="main">
    {activeComponent === PLOT && <PlotComponent  className="main"/>}
    {activeComponent === MEASURE && <MeasureComponent className="main"/>}
    
      </div>
      <ButtonBar setActiveComponent={setActiveComponent} className="footer" />
    </div>
  );
}

export default App;
