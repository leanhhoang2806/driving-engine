const express = require('express');
const { pool } = require('./db/db_instance');

// Create the app
const app = express();


const errorMiddleware = (handler) => async (req, res, next) => {
    try {
        await handler(req, res, next);
    } catch (error) {
        console.log(error);
        res.status(500).json({ error: 'Internal server error' });
    }
}

const authMiddleware = (req, res, next) => {
    const token = req.headers.authorization;
  
    if (!token) {
      return res.status(401).json({ error: 'Unauthorized: Missing token' });
    }
  
    try {
      const decoded = jwt.verify(token, SECRET_KEY);
      req.user = decoded; // Attach the user object to the request
      next();
    } catch (error) {
      return res.status(401).json({ error: 'Unauthorized: Invalid token' });
    }
  };

app.get('/status', (req, res) => {
    res.json({
        status: 'ok'
    })
})

app.get('/customer/:customerId', authMiddleware, errorMiddleware(async (req, res) => {
    const { customerId } = req.params;
    try{
        const { rows } = await pool.query('SELECT * FROM customer');
    } catch (error) {
        console.log(error);
        res.status(500).json({ error: 'Internal server error' });
    }
}))

// configs
const config = {
    port: 3000
}

app.listen(config.port, () => {
    console.log(`Server is running on port ${config.port}`);
})