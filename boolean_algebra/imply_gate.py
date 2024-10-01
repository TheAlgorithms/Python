const { existsSync, readFileSync } = require('fs');
const { resolve } = require('path');
const dotenv = require('dotenv');

// Load environment variables from .env file if it exists
const envPath = resolve(__dirname, '..', '.env');
if (existsSync(envPath)) dotenv.config({ path: envPath });
else console.warn(".env file not found. Using shell environment variables.");

// Destructure environment variables with default values
const { 
  NODE_ENV = 'production', 
  DEPLOYMENT_ENV = 'production', 
  MEMORY_LIMIT = '600M', 
  INSTANCE_COUNT = 'max' 
} = process.env;

// Handle module resolution issue for LoopBack if path exists
const loopbackModuleResolutionHack = resolve(__dirname, '../node_modules/.pnpm/node_modules');
if (!existsSync(loopbackModuleResolutionHack)) 
  console.error("LoopBack module path not found. Ensure dependencies are installed.");

module.exports = {
  apps: [{
    script: './lib/production-start.js',
    cwd: __dirname,
    env: { ...process.env, NODE_PATH: loopbackModuleResolutionHack },
    max_memory_restart: MEMORY_LIMIT,
    instances: INSTANCE_COUNT,
    exec_mode: 'cluster',
    name: DEPLOYMENT_ENV === 'staging' ? 'dev' : 'org',
    watch: false
  }]
};
