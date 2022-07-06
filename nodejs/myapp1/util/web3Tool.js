const Web3 = require("web3");
const web3 = new Web3(Web3.givenProvider || "ws://localhost:8545");

const ethEnabled = () => {
  if (window.ethereum) {
    window.web3 = new Web3(window.ethereum);
    window.ethereum.enable();
    return true;
  }
  return false;
}
module.exports = ethEnabled;