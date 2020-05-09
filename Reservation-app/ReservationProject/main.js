const { app, BrowserWindow } = require('electron')

function createWindow() {
    let win = new BrowserWindow({
        width: 1024,
        height: 768,
        webPreferences: {
            nodeIntegration: true
        }
    })

    // 그리고 앱의 index.html를 로드합니다.
    // win.loadFile('RSA.html')
    win.loadURL('http://localhost/reservation/revstart/')
}

app.whenReady().then(createWindow)