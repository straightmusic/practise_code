const basicAuth = require('basic-auth');

const auth = function(req, res, next) {
  // const user = basicAuth(req);
  // console.log(user);
  // if (!user || !user.name || !user.pass) {
  //   res.set('WWW-Authenticate', 'Basic realm=Authorization Required');
  //   res.sendStatus(401);
  // }
  // if (user.name === 'amy' && user.pass === 'passwd123') {
  //   next();
  // } else {
  //   res.set('WWW-Authenticate', 'Basic realm=Authorization Required');
  //   res.sendStatus(401);
  // }
  next();
}

module.exports = basicAuth;