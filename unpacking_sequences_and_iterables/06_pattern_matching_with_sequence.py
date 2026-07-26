# Example message: ['BEEPER', 440, 3]


def InvalidCommand(message):
    print(f"Error: {message}")


class Robot:
    def __init__(self, beep: str):
        self.beep = beep

    def beep(self, times, frequency): ...

    def rotate_neck(self, angle): ...

    def handle_command(self, message):
        match message:
            case ["BEEPER", frequency, times]:
                self.beep(times, frequency)
            case ["NECK", angle]:
                self.rotate_neck(angle)
            case ["LED", ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ["LED", ident, red, green, blue]:
                self.leds[ident,].set_color(ident, red, green, blue)
            case _:
                return InvalidCommand(message)
