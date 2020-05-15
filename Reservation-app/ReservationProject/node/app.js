const express = require('express')
const route = require('./routes') // routes/index.js 파일을 가져옴
const sequelize = require('./models').sequelize
sequelize.sync() // 데이터베이스에 생성해 준다 > DB Sync
const app = express();
app.use(express.json()) // json을 쓰겠다는 선언 --> 설정 안해주면 json을 못받음
app.use('/test_ori', () => {
    console.log('testing')
});

app.use('/', route) // /test 경로를 제외한 나머지는 모두 / 로 간다


app.listen(4000, () => {
    console.log('server is running');
});