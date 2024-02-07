"""Provide mqtt-remote functions."""
import json
from time import sleep, ticks_ms

from config import Config
from debounce import Debounce
from machine import Pin, reset
from net import NetworkManager
from uwebsockets import client as ws_client  # https://github.com/danni/uwebsockets

CONFIG = Config()
DEVICE_NAME = getattr(CONFIG, "DEVICE_NAME", "msmute")
WS_TOKEN = getattr(CONFIG, "WS_TOKEN", "")
WS_URI = getattr(CONFIG, "WS_URI", "")


def button_callback(pin, action):
    """Provide a callback for buttons."""
    print(pin, action)
    params = {
        "app": "msmute",
        "app-version": "1.0",
        "device": "wemos-d1-mini",
        "manufacturer": "jalmeroth",
        "protocol-version": "2.0.0",
        "token": f"{WS_TOKEN}",
    }
    paramstr = "&".join([f"{k}={v}" for k, v in params.items()])
    websocket = ws_client.connect(WS_URI, f"/?{paramstr}")
    if websocket is None:
        return
    data = {
        "action": action,
        "parameters": {},
        "requestId": 1,
    }
    request = json.dumps(data)
    websocket.send(request)
    print(f"> {request}")
    response = websocket.recv()
    print(f"< {response}")
    websocket.close()


def main():
    """Provide main routine."""
    # Setup the button input pin with a pull-up resistor.
    Debounce(Pin(14, Pin.IN), button_callback, action="toggle-hand")
    Debounce(Pin(12, Pin.IN), button_callback, action="toggle-mute")
    Debounce(Pin(13, Pin.IN), button_callback, action="toggle-video")
    Debounce(Pin(15, Pin.IN), button_callback, action="leave-call")

    ssid = getattr(CONFIG, "WIFI_SSID", "")
    password = getattr(CONFIG, "WIFI_PASS", "")
    NetworkManager().do_connect(ssid, password)

    while True:
        sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except OSError as err:
        print(f"Resetting: {err}")
        reset()
