const { app, BrowserWindow } = require('electron')

function createWindow() {
    let win = new BrowserWindow({
        width: 1300,
        height: 730,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadURL('http://localhost/reservation/revstart/')
}

app.whenReady().then(createWindow);
app.on('window-all-closed', () => {
    if (process.platform !== 'drawin')
        app.quit()
})
app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0)
        createWindow()
})