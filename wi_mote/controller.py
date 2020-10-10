from pyautogui import press
from wi_mote.media import VolumeController

volume_keys = (
    "vol_up",
    "vol_down",
    "toggle_mute"
)

player_keys = {
    "left": "left",
    "up": "up",
    "playpause": "space",
    "down": "down",
    "right": "right"
}


def handle_keypress(key):
    volume = VolumeController()

    if key in volume_keys:
        handler = volume.get_handler(key)
        handler()
    elif key in player_keys:
        press(player_keys.get(key))
