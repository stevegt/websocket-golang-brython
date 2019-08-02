from browser import alert, document, websocket

def on_open(evt):
    document['sendbtn'].disabled = False
    document['closebtn'].disabled = False
    document['openbtn'].disabled = True
    document['status'].value = "connected"

def on_message(evt):
    # message received from server
    # alert("Message received : {data}".format(data=evt.data))
    document["result"].value = evt.data

def on_close(evt):
    # websocket is closed
    # alert("Connection is closed")
    document['openbtn'].disabled = False
    document['closebtn'].disabled = True
    document['sendbtn'].disabled = True
    document['status'].value = "disconnected"

def _open(ev):
    if not websocket.supported:
        alert("WebSocket is not supported by your browser")
        return
    global ws
    # open a web socket
    # ws = websocket.WebSocket("wss://echo.websocket.org")
    ws = websocket.WebSocket("ws://localhost:8080/ws")
    # bind functions to web socket events
    ws.bind('open', on_open)
    ws.bind('message', on_message)
    ws.bind('close', on_close)

def send(ev):
    data = document["data"].value
    if data:
        ws.send(data)

def sendenter(ev):
    data = document["enterdata"].value
    if data:
        ws.send(data)

def sendlive(ev):
    data = document["livedata"].value
    if data:
        ws.send(data)

def mult(ev):
    multa = document["multa"].value
    multb = document["multb"].value
    if len(multa) > 0 and len(multb) > 0: 
        multa = float(multa)
        multb = float(multb)
    else:
        return
    res = multa * multb
    document['result'].value = res

def close_connection(ev):
    ws.close()
    document['openbtn'].disabled = False

ws = None
document["openbtn"].bind("click", _open)
document["sendbtn"].bind("click", send)
document["closebtn"].bind("click", close_connection)
document["enterdata"].bind("change", sendenter)
document["livedata"].bind("keyup", sendlive)
document["multa"].bind("change", mult)
document["multb"].bind("change", mult)
document["status"].value = __name__
