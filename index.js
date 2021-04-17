const net = require('net');
const fs = require('fs');

const checkField = (field) => {
    const a = field.split(".");
    if (a[0] && a[1] && a[0] != "" && a[1] != "") {
        return true;
    }
    return false;
}

const server = net.createServer((c) => {
    // 'connection' listener.
    console.log('client connected');
    c.on('end', () => {
        console.log('client disconnected');
    });
    /*     c.write('hello\r\n');
        c.pipe(c); */
    c.on('data', (data) => {
        const a = data.toString().split(";");
        for (let [d, c] of a.entries()) {
            //console.log(c, d);
            if ((d) % 3 == 0) {
                if (a[d] - a[d - 3] > 50) continue;
                if (a[d + 1] - a[d + 1 - 3] > 50) continue;
                if (a[d + 2] - a[d + 2 - 3] > 50) continue;

                if (a[d] && a[d + 1] && a[d + 2] && checkField(a[d]) && checkField(a[d + 1]) && checkField(a[d + 2])) {
                    fs.appendFileSync('valori.txt', `${a[d]};${a[d + 1]};${a[d + 2]};\n`);
                }
            }
        }
    });
});



server.on('error', (err) => {
    console.log(err)
});

server.listen(5560, () => {
    console.log('server bound');
});