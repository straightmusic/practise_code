const express = require('express');
const basicAuth = require('express-basic-auth');
const web3Tool = require('../util/web3Tool.js');
const router = express.Router();

// middleware that is specific to this router
router.use(function timeLog(req, res, next) {
  console.log('Time: ', Date.now());
  next();
});

// define the about route
router.get('/sayHello', function(req, res) {
  console.log('sayHello');
  res.send("sayHello");
});

router.get('/MetaMaskConnect', function(req, res) {
  web3Tool();
  res.end();
});

module.exports = router;

// const api = {
//   "/api/sayHello": function(request, response, requestUrl) {
//     const URLSearchParams = requestUrl.searchParams;
//     let data = {
//       "result": "Hello World"
//     };
//     URLSearchParams.forEach((v, k) => {
//       data[k] = v;
//     });
//
//     response.statusCode = 200;
//     response.setHeader("Content-Typ", "application/json");
//     response.end(JSON.stringify(data));
//   }
// };
//
// module.exports = api;