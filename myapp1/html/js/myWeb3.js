const web3 = require('web3');
const ethEnabled = () => {
  if (window.ethereum) {
    window.web3 = new Web3(window.ethereum);
    window.ethereum.enable();
    return true;
  }
  return false;
}
$(".ethEnabled").click(function() {
  console.log("sss");
  ethEnabled();
})