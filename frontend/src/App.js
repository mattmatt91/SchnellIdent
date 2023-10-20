// App.js
import './App.css';
import Header from './components/Header';
import ButtonBar from './components/ButtonBar';
import MeasureComponent from './components/MeasureComponent';
import PlotComponent from './components/PlotComponent';
import React, { useState } from 'react';

function App() {
  const [activeComponent, setActiveComponent] = useState(null);

  return (
    <div className="app">
      <Header />
      <div className="canvas-container">
        {activeComponent === 'measure' && <MeasureComponent />}
        {activeComponent === 'plot' && <PlotComponent />}
      </div>
      <ButtonBar setActiveComponent={setActiveComponent} />
    </div>
  );
}

export default App;
