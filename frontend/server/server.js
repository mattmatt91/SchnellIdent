// server/routes.js
const express = require('express');
const router = express.Router();

// Sample data for measurement IDs
const measurementIds = ['measurement1', 'measurement2', 'measurement3'];

// Sample data for measurements (you can replace this with your actual data)
const measurements = {
  measurement1: [{ timestamp: 1, value: 10 }, { timestamp: 2, value: 20 }],
  measurement2: [{ timestamp: 1, value: 15 }, { timestamp: 2, value: 25 }],
  measurement3: [{ timestamp: 1, value: 5 }, { timestamp: 2, value: 15 }],
};

// Route to get a list of measurement IDs
router.get('/get_all_ids', (req, res) => {
  res.json(measurementIds);
});

// Route to get measurement data by ID
router.get('/get_measurement/:id', (req, res) => {
  const id = req.params.id;
  const data = measurements[id];

  if (data) {
    res.json(data);
  } else {
    res.status(404).json({ error: 'Measurement not found' });
  }
});

module.exports = router;
