
// simple node usage
const axios = require('axios');
const base = process.env.BASE || 'http://localhost:8000';

(async () => {
  console.log((await axios.get(base + '/')).data);
  console.log((await axios.get(base + '/discover/')).data);
  console.log((await axios.post(base + '/verify-number/', { number: '+911234567890' })).data);
})();
