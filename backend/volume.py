from alsaaudio import Mixer
from os import system


class VolumeController:
    def __init__():
        self.mixer = Mixer()

        # get the current volume settings
        self.current_vol = mixer.getvolume()[0]
        self.is_muted = mixer.getmute()[0]


    def toggle_mute():
        if self.is_muted:
            self.mixer.setmute(False)
        else:
            self.mixer.setmute(True)


    def volume_up():
        self.current_vol += 5
        if value > 100:
            value = 100
        self.mixer.setvolume(value)


    def volume_up():
        self.current_vol -= 5
        if value < 0:
            value = 0
        self.mixer.setvolume(value)


class MediaController:
    '''
    Class housing custom functions for media controls.
    '''

    def __init__():
        self.cmd = "xdotool key --clearmodifiers"
        self.media_commands = {
            "toggle": "XF86AudioPlay",
            "forward": "XF86AudioNext"
            "backward": "XF86AudioPrev"
        }


    def pause():
        system(f"{self.cmd} {self.media_commands.get("toggle")}")


    def forward():
        system(f"{self.cmd} {self.media_commands.get("forward")}")


    def rewind():
        system(f"{self.cmd} {self.media_commands.get("backward")}")
