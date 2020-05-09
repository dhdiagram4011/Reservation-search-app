const { app, BrowserWindow } = require('electron')

function createWindow() {
    let win = new BrowserWindow({
        width: 1300,
        height: 768,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadURL('http://localhost/reservation/revstart/')
}

app.whenReady().then(createWindow)