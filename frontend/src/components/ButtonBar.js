// ButtonBar.js
import './ButtonBar.css';
import React from 'react';

function ButtonBar({ setActiveComponent }) {
    return ( <
        div className = "button-bar" >
        <
        button className = "button"
        onClick = {
            () => setActiveComponent('measure')
        } >
        Measure <
        /button> <
        button className = "button"
        onClick = {
            () => setActiveComponent('plot')
        } >
        Data <
        /button> < /
        div >
    );
}

export default ButtonBar;