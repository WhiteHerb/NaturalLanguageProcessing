const express = require('express');
const app = express();
const port = process.env.port || 3000
const {PythonShell} = require('python-shell');
const router = express.Router();

var loaddata;

app.get('/', (req,res) => res.send('this is weh to connect node ans python'))

app.all('/processing/:id/:ids', (req,res) =>{
    let pyoption = {
        scriptPath: "/home/nel951/program/discored bot/discord.py-luna/",
        args: [req.params.id,req.params.ids]
    }
    PythonShell.run("netural_process.py",pyoption, (err,data) =>{
        if (err) throw err;
        loaddata = data;
        console.log(req.params.ids);
        console.log(loaddata);
    })
    setTimeout(() => {
        res.send("<h1>" + loaddata + "<h1>")
    }, 3000);
    
})

app.listen(port, () => console.log('start in' + port))