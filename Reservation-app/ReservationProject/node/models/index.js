const Sequelize = require('sequelize');
//const config = require('../config/config');
const db = {}; //DB를 넣을 빈 폴더 - DB 라는 객체를 생성 , db에서 꺼내와서 Create 함
const sequelize = new Sequelize(
    "test", //데이터베이스 이름
    "aaa", // 아이디
    "0000", {
        //host랑 dialect는 무조건 객체로 넣어야함
        host: "18.223.132.93",
        dialect: "mysql" //어떤 데이터 베이스를 사용가는가
    }
);
db.sequelize = sequelize;
db.Sequelize = Sequelize;

//생성할 DB테이블 연결
const Board = require('./Board')(sequelize, Sequelize);
// const User = require('./User')(sequelize, Sequelize); - User 생성
db.Board = Board;
//db.User = User; 

// User.hasMany(Board, { as: 'author' });
module.exports = db;