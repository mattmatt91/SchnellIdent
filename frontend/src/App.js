import './App.css';
// App.js


import Header from './components/HeaderComponent/HeaderComponent';
import ButtonBar from './components/ButtonBarComponent/ButtonBarComponent';
import MeasureComponent from './components//MeasureComponent/MeasureComponent';
import PlotComponent from './components/DataComponent/DataComponent';
import React, { useState } from 'react';

function App() {
  const [activeComponent, setActiveComponent] = useState(null);
  
  return (
    <div className="app">

      <Header className="header" />

      {activeComponent === 'plot' && <PlotComponent className="main" />}
      {activeComponent === 'measure' && <MeasureComponent className="main" />}

      <ButtonBar setActiveComponent={setActiveComponent} className="footer" />

    </div>
  );
}

export default App;
