
#!/usr/bin/env node
const { Command } = require('commander');
const axios = require('axios');
const pkg = require('./package.json');
const program = new Command();

program.version(pkg.version);

program.option('-b, --base <url>', 'Base URL of the backend', 'http://localhost:8000');

program
  .command('discover')
  .description('Discover available services')
  .action(async (opts) => {
    const base = program.opts().base;
    try {
      const res = await axios.get(`${base}/discover/`);
      console.log(JSON.stringify(res.data, null, 2));
    } catch (e) {
      console.error('Error:', e.message);
    }
  });

program
  .command('verify-number')
  .description('Verify a phone number')
  .requiredOption('-n, --number <number>', 'Phone number to verify (E.164 preferred)')
  .action(async (cmd) => {
    const base = program.opts().base;
    try {
      const res = await axios.post(`${base}/verify-number/`, { number: cmd.number });
      console.log(JSON.stringify(res.data, null, 2));
    } catch (e) {
      console.error('Error:', e.message);
    }
  });

program
  .command('simswap')
  .description('Run a SIM-swap risk check')
  .requiredOption('-n, --number <number>', 'Phone number to check')
  .action(async (cmd) => {
    const base = program.opts().base;
    try {
      const res = await axios.post(`${base}/simswap/`, { number: cmd.number });
      console.log(JSON.stringify(res.data, null, 2));
    } catch (e) {
      console.error('Error:', e.message);
    }
  });

program.parse(process.argv);
