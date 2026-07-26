class Observer:
    def update(self, message):
        print(f"Se recibio el mensaje: {message}")


class YoutubeChannel:
    def __init__(self) -> None:
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)


obs1 = Observer()
obs2 = Observer()

midudev = YoutubeChannel()
midudev.subscribe(obs1)
midudev.subscribe(obs2)
midudev.notify("Nuevo video")
