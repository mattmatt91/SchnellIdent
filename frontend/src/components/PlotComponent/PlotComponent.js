import React from 'react';
import Plot from 'react-plotly.js';
import './PlotComponent.css';

function DataPlotComponent({ data }) {
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
            line: { color: 'white' },
          },
        ]}
        layout={{
          xaxis: {
            title: 'Time (s)',
            tickfont: { color: 'white' },
            titlefont: { color: 'white' },
            showline: true,
            showticklabels: true,
          },
          yaxis: {
            title: 'Volts',
            tickfont: { color: 'white' },
            titlefont: { color: 'white' },
            showline: true,
            showticklabels: true,
          },
          paper_bgcolor: 'black',
          plot_bgcolor: 'black',
          showlegend: false,
          autosize: true,
          margin: { l: 0, r: 0, t: 0, b: 0 },
        }}
      />
    </div>
  );
}

export default DataPlotComponent;
