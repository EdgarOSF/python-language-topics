# Example message: ['BEEPER', 440, 3]

class Robot:
    def __init__(self, beep: str):
        self.beep = beep


    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                self.leds[ident,].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)
