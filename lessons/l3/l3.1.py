

from abc import ABC, abstractclassmethod

class Animal(ABC):

    @abstractclassmethod
    def make_sound(self):
        pass
    @abstractclassmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("imma dogy")

    def move(self):
        print("5 kilometers")

class Fish(Animal):

    def make_sound(self):
        print("bul' bul'")

    def move(self):
        print("drowing")

    # new subclasses
dog = Dog()
fish = Fish()

dog.move()
fish.move()

class AbstractOtpSender(ABC):

    @abstractclassmethod
    def send_sms_to_phone(self):
        pass

class KG_SenderSms(AbstractOtpSender):
    def send_sms_to_phone(self):
        pass