from alsaaudio import Mixer, mixers


class VolumeController:
    def __init__(self):
        # `Mixer` defaults to 'Master' 
        # `mixers()` gives all available volume controls
        self.mixer = Mixer(mixers()[0])
        # get the current volume
        self.current_vol = self.mixer.getvolume()[0]

    def get_handler(self, key):
        mapping = {
            'toggle_mute': self.toggle_mute,
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
        if self.current_vol > 100:
            self.current_vol = 100
        self.mixer.setvolume(self.current_vol)

    def volume_down(self):
        self.current_vol -= 5
        if self.current_vol < 0:
            self.current.vol = 0
        self.mixer.setvolume(self.current_vol)
