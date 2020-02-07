function sendDataToServer(fullIPAndPort, dataToSend) {
    let socket = new WebSocket(fullIPAndPort);
    console.log("[Communications] : Opening communications")
    
    socket.onopen = function (e) {
        socket.send(dataToSend);
        console.log("[Communications] : Sent data successfully")
        socket.close();
    };
    socket.onclose = function (event) {
        console.log("[Communications] : Closed communications")
    };
}

sendDataToServer("ws://localhost:5555/", "rotatehead(forward);turn(left);move(forward);turn(left);");