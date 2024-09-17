const { createServer } = require('http');
const countStudents = require('./3-read_file_async');
const path = require('path');

const hostname = '127.0.0.1';
const port = 1245;

const app = createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  }

  else if (req.url === '/students') {
    res.statusCode = 200;
    try {
        let data = 'This is the list of our students\n';
        const databasePath = path.join(__dirname, 'database.csv');
        const studentsData = await countStudents(databasePath);
        data += studentsData;
        res.end(data);
    } catch (err) {
        res.statusCode = 500;
        res.end('Cannot load the database');
    }
  }

});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;