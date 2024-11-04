import React, { useState } from 'react';
import './VideoPlayerComponent.css'; // Optional: create this file for custom styles

function VideoPlayerComponent() {
  const [showVideo, setShowVideo] = useState(false);

  const handleVideoStart = () => {
    setShowVideo(true);
  };

  return (
    <div className='video-player'>
      <button className="button" onClick={handleVideoStart} style={{ marginTop: '10px' }}>
        Start Video
      </button>
      {showVideo && (
        <div className="video-container">
          <video controls width="600">
            <source src="ManualVid.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      )}
    </div>
  );
}

export default VideoPlayerComponent;
