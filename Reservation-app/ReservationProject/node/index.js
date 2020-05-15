const express = require('express')
const app = express();

app.use('/test', () => {
    console.log('testing')
});


app.listen(4000, () => {
    console.log('server is running');
});

