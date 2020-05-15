const express = require('express'); //모듈로 부터 express를 불러움
const router = express.Router() //GET.POST 이용가능
const models = require("../models")
router.post('/board', async(req, res, next) => {
        console.log('test post 입니다')
            // const title = req.body.title
            // const content = req.body.content
        const { title, content } = req.body
        await models.Board.create({ title: title, content: content }) // response를 죽이지 않고 기다려줌, 기준이 Response는 아님
        res.status(200).json({
            'success': "success",
            "title": title,
            "content": content
        })
    }) //post로 온 TEST 를 받는다
router.get('/board', async(req, res, next) => {
        console.log('test get 입니다')
        const findBoard = await models.Board.findAll() //array 로 묶음 - findAll
        res.status(200).json({ success: "success", findBoard })
    }) //get 으로 온 board 를 받는다

module.exports = router