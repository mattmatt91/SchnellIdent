import React from 'react';
import Plot from 'react-plotly.js';
import './DataPlotComponent.css'; //


function DataPlotComponent({ data }) {
    // console.log(data)
    const timestampData = data.map((point) => point.timestamp);
    const irData = data.map((point) => point.IR);
    const micData = data.map((point) => point.MIC);

    return ( <
        div className = "data-plot" >
        <
        Plot data = {
            [{
                    x: timestampData,
                    y: irData,
                    type: 'scatter',
                    mode: 'lines',
                    name: 'IR',
                    line: { color: 'red' },
                },
                {
                    x: timestampData,
                    y: micData,
                    type: 'scatter',
                    mode: 'lines',
                    name: 'MIC',
                    line: { color: 'green' },
                },
            ]
        }
        layout = {
            {
                xaxis: {
                    title: 'Time (s)',
                    tickfont: { color: 'white' }, // Set tick font color to white
                    titlefont: { color: 'white' }, // Set title font color to white
                    showline: true, // Display axis line
                    showticklabels: true, // Display tick labels
                },
                yaxis: {
                    title: 'Volts',
                    tickfont: { color: 'white' }, // Set tick font color to white
                    titlefont: { color: 'white' }, // Set title font color to white
                    showline: true, // Display axis line
                    showticklabels: true, // Display tick labels
                },
                paper_bgcolor: 'black', // Set the background color of the plot to black
                plot_bgcolor: 'black', // Set the background color of the plot area to black
                showlegend: false, // Hide the legend
                autosize: true, // Full width of the page
                margin: { l: 0, r: 0, t: 0, b: 0 }, // Remove margins
            }
        }
        /> <
        /div>
    );
}

export default DataPlotComponent;