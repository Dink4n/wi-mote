from os import system
from pyautogui import press

volume_cmd = "amixer -c 1 set Master"
volume_keys = {
    # name  | cmd
    "up"  : "10+",
    "down": "10-",
    "mute": "toggle",
}

player_keys = {
    # name  | cmd
    "rewind" : "left",
    "pause"  : "space",
    "forward": "right"
}
utility_keys = {
    # name  | cmd
    #FIXME: poweroff isn't working at the moment
    "poweroff": "kill $(pidof flask && pidof npm)"
}


def handle_keypress(key):
    try:
        if key in volume_keys:
            tmp_cmd = f"{volume_cmd} {volume_keys.get(key)}"
            system(tmp_cmd)
        elif key in player_keys:
            press(player_keys.get(key))
        elif key in utility_keys:
            tmp_cmd = utility_keys.get(key)
            system(tmp_cmd)
        return True
    except:
        return False
