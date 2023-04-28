"""Provide mqtt-remote functions."""
import json
from machine import Pin, reset
from time import sleep, ticks_ms

from net import NetworkManager
from config import Config
from debounce import Debounce
from uwebsockets import client as ws_client  # https://github.com/danni/uwebsockets


CONFIG = Config()
DEVICE_NAME = getattr(CONFIG, "DEVICE_NAME", "msmute")
WS_TOKEN = getattr(CONFIG, "WS_TOKEN", "")
WS_URI = getattr(CONFIG, "WS_URI", "")

ACTIONS = {
    "toggle-hand": "raise-hand",
    "toggle-mute": "toggle-mute",
    "toggle-video": "toggle-video",
    "leave-call": "call",
    "query-meeting-state": "query-meeting-state",
}


def button_callback(pin, action):
    """Provide a callback for buttons."""
    print(pin, action)
    # action = "query-meeting-state"
    websocket = ws_client.connect(f"{WS_URI}?token={WS_TOKEN}")
    if websocket is None:
        return
    data = {
        "apiVersion": "1.0.0",
        "service": ACTIONS[action],
        "action": action,
        "timestamp": ticks_ms(),
        "manufacturer": "Elgato",
        "device": "Stream Deck",
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
