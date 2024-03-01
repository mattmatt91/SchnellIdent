// HeaderComponent.js

import React from 'react';
import './HeaderComponent.css';

function Header({ toggleFullscreen }) {
  return (
    <div className="header">
      <img src="logo.jpg" alt="Ascot" />
      <button onClick={toggleFullscreen} className="fullscreen-toggle">Toggle Fullscreen</button>
    </div>
  );
}

export default Header;
