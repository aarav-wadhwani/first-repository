import json
# import websocket as ws

# dict to define json
requestdict = {
    "method": "SUBSCRIBE",
    "params": ["btcusdt@aggTrade"],
    "id": 1
}
requestjson = json.dumps(requestdict)
print(requestjson)


import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

# we recieve something from the server
def on_message(ws, message):
    print(message)

# if something goes wrong
def on_error(ws, error):
    print(error)

# when websocket is closed
def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

# when websocket is open
def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send(requestjson)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    # creates new thread
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://fstream.binance.com/ws/BTCUSDT@aggTrade/",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()

