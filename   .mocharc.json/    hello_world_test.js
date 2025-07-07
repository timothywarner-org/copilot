{
  "spec": "test/**/*.js",
  "timeout": 5000,
  "reporter": "spec"
} 

const assert = require('assert');
describe('Application', () => {
  it('should run correctly', () => {
    assert.strictEqual(true, true);
  });
});