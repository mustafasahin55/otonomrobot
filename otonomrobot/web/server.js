const express = require('express');
const { version, Chip, Line } = require('node-libgpiod');

const app = express();
const port = 3000;

// Motor kontrolü için GPIO pinlerini ayarlayın
//const forwardPin = new Gpio(17, 'out'); // Örneğin GPIO17
//const backwardPin = new Gpio(27, 'out'); // Örneğin GPIO27

global.chip = new Chip(0);
global.line = new Line(chip, 17);
line.requestOutputMode();


app.get('/', (req, res) => {
    res.send(`
    <html>
    <style>
    .center-div {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
    }

    button {
        margin: 10px;
        padding: 10px 20px;
        font-size: 20px
    }
    </style>
      <body>
        <div class="center-div">
            <button onclick="move('forward')">Move forward</button>
            <button onclick="move('backward')">Move backwards</button>
        </div>
      <script>
        function move(direction) {
            fetch('/move/' + direction);
        }
      </script>
        </body>
    </html>
  `);
});

app.get('/move/:direction', (req, res) => {
    if (req.params.direction === 'forward') {
        line.setValue(1);
       // setTimeout(,1000);
    } else if (req.params.direction === 'backward') {
       // forwardPin.writeSync(0);
       // backwardPin.writeSync(1);
    }
    res.send('Moving ' + req.params.direction);
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});

//process.on('SIGINT', () => {
  //forwardPin.unexport();
 // backwardPin.unexport();
//});

