import React, { useState, useLayoutEffect } from 'react';
import Plot from 'react-plotly.js';
import './PlotComponent.css';

function DataPlotComponent({ data }) {
  const [dimensions, setDimensions] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useLayoutEffect(() => {
    function handleResize() {
      setDimensions({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const timestampData = data.map((point) => point.timestamp);
  const irData = data.map((point) => point.IR);
  const micData = data.map((point) => point.MIC);

  return (
    <div className="data-plot">
      <Plot
  data={[
    {
      x: timestampData,
      y: irData,
      type: 'scatter',
      mode: 'lines',
      name: 'IR',
      line: { color: 'grey' },
    },
    {
      x: timestampData,
      y: micData,
      type: 'scatter',
      mode: 'lines',
      name: 'MIC',
      line: { color: 'red' },
    },
  ]}
  layout={{
    width: 600,  // Fixed width for the plot
    height: 350, // Fixed height for the plot
    xaxis: {
      title: 'Time (s)',
      showline: true,
      showticklabels: true,
    },
    yaxis: {
      title: 'Volts',
      showline: true,
      showticklabels: true,
    },
    paper_bgcolor: 'black',
    plot_bgcolor: 'black',
    showlegend: false,
    autosize: false, // Disable autosize to ensure fixed dimensions
    margin: { l: 0, r: 0, t: 0, b: 0 },
  }}
/>

    </div>
  );
}

export default DataPlotComponent;
