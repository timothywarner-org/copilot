const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('blog', { title: 'Blog' });
});

module.exports = router;