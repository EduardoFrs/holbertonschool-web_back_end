var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.send('Hello Holberton School!')
})

app.listen(1245)
