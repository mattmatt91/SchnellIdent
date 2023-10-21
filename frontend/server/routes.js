const express = require('express');
const cors = require('cors');

const app = express();

// Use the CORS middleware to allow requests from http://localhost:3000
app.use(cors({ origin: 'http://localhost:3000' }));

// ... Other server setup and routes

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
