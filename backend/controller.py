from backend.media import VolumeController, MediaController

volume_keys = {
    # name  | cmd
    "up"  : "5+",
    "down": "5-",
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
    volume = VolumeController()

    try:
        if key in volume_keys:
            pass
        elif key in player_keys:
            press(player_keys.get(key))
        elif key in utility_keys:
            print("Sorry poweroff not working at the moment")
        return True
    except:
        return False
