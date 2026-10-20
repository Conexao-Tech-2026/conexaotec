const http = require('http');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {

const host = req.headers['host'] || 'Desconhecido';
	
const ip =
    req.headers['x-real-ip'] ||
    req.headers['x-forwarded-for']?.split(',')[0].trim() ||
    req.socket.remoteAddress;

console.log(`IP do cliente: ${ip}`);
	
    res.statusCode = 200;
	    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.end(`
        <h1>Hello from Node 1</h1>
        <p>Seu IP é: <strong>${ip}</strong></p>
	    <p>Host da requisição: ${host}</p>
    `);
	
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
