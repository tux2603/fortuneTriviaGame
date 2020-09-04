let socket = new WebSocket("ws://localhost:1337");

function sendCode(code) {
    socket.send(JSON.stringify({'code': code}));
}

socket.onopen = function(e) {
};

socket.onmessage = function(event) {
    console.log(event.data);
    var data = JSON.parse(event.data);
    console.log(`[message] Data received from server: ${data}`);
};

socket.onclose = function(event) {
    var data = JSON.parse(event.data);
    if (event.wasClean) {
        console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    } else {
        // e.g. server process killed or network down
        // event.code is usually 1006 in this case
        console.log('[close] Connection died');
    }
};

socket.onerror = function(error) {
    console.log(`[error] ${error.message}`);
};