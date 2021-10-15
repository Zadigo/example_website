import Vue from 'vue'

Vue.config.productionTip = false

// Get all the test functions in the ./modules directory
const testFiles = require.context('./unit', true, /^Test.*/)
testFiles.keys().forEach(testFiles)

// Get all the src .vue files except for main.js
const srcContext = require.context('../../src', true, /^\.\/(?!main(\.js)?$)/);
srcContext.keys().forEach(srcContext);
