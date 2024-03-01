import React, { useState, useEffect } from 'react';
import './HeaderComponent.css';

function Header({ toggleFullscreen }) {
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    const updateFullscreenState = () => {
      // Check the fullscreen element of the document to determine fullscreen state
      const isNowFullscreen = Boolean(document.fullscreenElement);
      setIsFullscreen(isNowFullscreen);
    };

    // Listen for fullscreen changes and keydown events
    document.addEventListener('fullscreenchange', updateFullscreenState);
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && isFullscreen) {
        // If fullscreen is active and ESC is pressed, exit fullscreen
        toggleFullscreen();
      }
    });

    return () => {
      document.removeEventListener('fullscreenchange', updateFullscreenState);
    };
  }, [isFullscreen, toggleFullscreen]);

  return (
    <div className="header">
      <img src="logo.jpg" alt="Company Logo" />
      {!isFullscreen && (
        <button onClick={() => {
          toggleFullscreen();
          setIsFullscreen(true);
        }} className="fullscreen-toggle">
          Toggle Fullscreen
        </button>
      )}
    </div>
  );
}

export default Header;
