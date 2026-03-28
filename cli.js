#!/usr/bin/env node
/**
 * OpenClaw Trading Assistant - Node.js Wrapper
 * 
 * This script wraps the Python CLI for npm distribution
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

// 检查 Python 是否安装
function checkPython() {
  return new Promise((resolve, reject) => {
    const python = spawn(process.platform === 'win32' ? 'python' : 'python3', ['--version']);
    
    python.on('error', (err) => {
      reject(new Error('Python is required but not installed. Please install Python 3.11+'));
    });
    
    python.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error('Python 3.11+ is required'));
      }
    });
  });
}

// 运行 Python CLI
function runCLI(args) {
  const scriptPath = path.join(__dirname, 'cli.py');
  const pythonCmd = process.platform === 'win32' ? 'python' : 'python3';
  
  const python = spawn(pythonCmd, [scriptPath, ...args], {
    stdio: 'inherit',
    cwd: __dirname
  });
  
  python.on('error', (err) => {
    console.error('❌ Failed to start Python:', err.message);
    process.exit(1);
  });
  
  python.on('close', (code) => {
    process.exit(code);
  });
}

// 主函数
async function main() {
  try {
    await checkPython();
    const args = process.argv.slice(2);
    runCLI(args);
  } catch (err) {
    console.error('❌ Error:', err.message);
    console.error('\n📦 This package requires Python 3.11+');
    console.error('   Install Python from: https://www.python.org/downloads/');
    process.exit(1);
  }
}

main();
