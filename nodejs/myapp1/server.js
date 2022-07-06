const api_dir = './api';
const util_dir = './util';

const express = require('express');
const fs = require('fs')
const api = require(api_dir + '/myApi.js');
const auth = require(util_dir + '/auth.js');

const port = 3000;
const ip = '127.0.0.1';
const HttpAction = new Object();
const app = express();

app.use(express.static('html')); // can use ./html file
app.use('/api', api);

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})