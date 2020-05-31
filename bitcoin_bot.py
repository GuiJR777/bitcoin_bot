import ssl
import json

import websocket


def sell():
    pass


def buy(amount):
    pass


def on_open(ws):
    print("Opened")
    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """
    ws.send(json_subscribe)


def on_closer(ws):
    print("Closed")


def on_error(ws, error):
    print("Error")
    print(error)


def on_message(ws, message):
    message = json.loads(message)
    price = message["data"]["price"]
    print(price)

    if price > 10000:
        sell()
    elif price < 9000:
        buy()
    else:
        print("Wait")


if __name__ == '__main__':
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net/",
                                on_open=on_open,
                                on_close=on_closer,
                                on_message=on_message,
                                on_error=on_error)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
