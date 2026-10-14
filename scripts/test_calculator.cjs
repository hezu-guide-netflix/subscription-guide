const assert = require('node:assert/strict');
const {calculate} = require('../assets/calculator.js');
assert.deepEqual(calculate(100,26,90,5), {total:95, daily:95/26, per30:95/26*30});
assert.equal(calculate(28,26,100,0).per30.toFixed(2),'32.31');
assert.equal(calculate(240,365,100,0).per30.toFixed(2),'19.73');
assert.equal(calculate(0,30,100,0).total,0);
for(const args of [[10,0,100,0],[10,-1,100,0],[10,2.5,100,0],[-1,30,100,0],[10,30,101,0],[10,30,0,0],[Infinity,30,100,0],[10,30,100,-1],[NaN,30,100,0]]) assert.throws(()=>calculate(...args));
console.log('PASS: discount, extra fees, unequal durations, zero price and invalid inputs');
assert.throws(()=>calculate(1e308,1,100,0));
