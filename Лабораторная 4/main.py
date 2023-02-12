class Animal:
    """Класс описывающий животное """
    def __init__(self, sound: str = "???"):
        """Инициализация экземпляра класса.
           :param sound: "Голос" животного
         """
        self.sound = sound

    def voice(self) -> None:
        """ Метод выводит звук, который издает животное в консоль.
        """
        pass

    def __repr__(self) -> str:
        """ Метод выводит имя класса консоль."""
        return f'{self.__class__.__name__}'

    def __str__(self):
        """ Метод выводит информацию о том, какой звук издает животное."""
        return f'Животное которое говорит "{self.sound}"'


class Cat(Animal):
    """Класс описывающий животное кошку"""
    legs = 4

    def __init__(self, name: str = "Unnamed"):
        """Инициализация экземпляра класса.
        :param name: Кличка кошки
        """
        super().__init__("Мяу")
        self.name = name


if __name__ == "__main__":
    # Write your solution here
    pass
