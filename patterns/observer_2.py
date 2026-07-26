from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class Subject:
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class EmailSender(Observer):
    def update(self, data):
        print(f"Email send: {data}")


class SMSSender(Observer):
    def update(self, data):
        print(f"SMS send: {data}")


class RSSSender(Observer):
    def update(self, data):
        print(f"RSS send: {data}")


sub = Subject()

sendEmail = EmailSender()
sendSMS = SMSSender()
sendRSS = RSSSender()

sub.attach(sendEmail)
sub.attach(sendSMS)
sub.attach(sendRSS)

sub.notify("Este es un mensaje importante.")
