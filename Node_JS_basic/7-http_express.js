const express = require('express');
const app = express();
const fs = require('fs/promises');
const path = require('path');

const countStudents = require('./3-read_file_async');

app.get('text/plain')

app.get('/', function (req, res) {
    res.send('Hello Holberton School!')
})

app.get('/students', async (req, res) => {
    try {
      const filePath = path.join(__dirname, 'database.csv');
      const studentsData = await countStudents(filePath);
      const response = `This is the list of our students\n${studentsData}`;
      res.send(response);
    } catch (error) {
        res.send('Cannot load the database')
    };
})

app.listen(1245)

module.exports = app;
