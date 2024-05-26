import { defineConfig } from 'vite';
const path = require('path')


export default defineConfig({
  root: './src',
  resolve: {
    alias: {
      '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
    }
  },
  build: {
    target: 'esnext',
    manifest: true,
    polyfillDynamicImport: false,
    minify: true,
    outDir: '../front', 
  },
});