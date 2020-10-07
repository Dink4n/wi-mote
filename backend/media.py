from alsaaudio import Mixer
from os import system


class VolumeController:
    def __init__(self):
        self.mixer = Mixer()
        # get the current volume
        self.current_vol = self.mixer.getvolume()[0]

    def get_key(self, key):
        mapping = {
            'mute': self.toggle_mute,
            'vol_up': self.volume_up,
            'vol_down': self.volume_down,
        }
        return mapping.get(key)

    def toggle_mute(self):
        if self.mixer.getmute()[0]:
            self.mixer.setmute(False)
        else:
            self.mixer.setmute(True)

    def volume_up(self):
        self.current_vol += 5
        if self.value > 100:
            value = 100
        self.mixer.setvolume(value)

    def volume_down(self):
        self.current_vol -= 5
        if self.value < 0:
            value = 0
        self.mixer.setvolume(value)


class MediaController:
    '''
    Class housing custom functions for media controls.
    '''

    def __init__(self):
        self.cmd = "xdotool key --clearmodifiers"
        self.media_commands = {
            "toggle": "XF86AudioPlay",
            "forward": "XF86AudioNext",
            "backward": "XF86AudioPrev"
        }

    def get_key(self, key):
        mapping = {
            'pause': self.pause,
            'forward': self.forward,
            'rewind': self.rewind,
        }
        return mapping.get(key)

    def pause(self):
        system(f"{self.cmd} {self.media_commands.get('toggle')}")

    def forward(self):
        system(f"{self.cmd} {self.media_commands.get('forward')}")

    def rewind(self):
        system(f"{self.cmd} {self.media_commands.get('backward')}")
