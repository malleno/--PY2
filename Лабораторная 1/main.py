# TODO Написать 3 класса с документацией и аннотацией типов
import string


class Tree:
    def __init__(self, branches: int = 0, leafs: int = 0):
        """Инициализация экземпляра класса.
           :param branches: Количество веток
           :param leafs: Количество листьев
         """

        if not isinstance(leafs, int):
            raise TypeError
        if leafs < 0:
            raise ValueError

        if not isinstance(branches, int):
            raise TypeError
        if branches < 0:
            raise ValueError

        self.root = 1
        self.branches = branches
        self.leafs = leafs

    def grow_leafs(self, amount_of_new_leafs: int) -> None:
        """
        Метод увеличивает количество листьев у дерева и возвращает их количество.
        :param amount_of_new_leafs: Количество новых листьев
        :return: int
        >>> tree = Tree(10, 20)
        >>> tree.grow_leafs(30)
        50
        """
        if not isinstance(amount_of_new_leafs, int):
            raise TypeError
        if amount_of_new_leafs < 0:
            raise ValueError
        self.leafs += amount_of_new_leafs
        return self.leafs

    def chopped(self) -> None:
        """ Метод вырубает дерево, остается только корень."""

        self.branches = 0
        self.leafs = 0


class Rational:
    def __init__(self, numerator: int = 0, denumenator: int = 1):
        """Инициализация экземпляра класса.
           :param numerator: Числитель
           :param denumenator: Знаменатель
         """
        if not isinstance(numerator, int):
            raise TypeError

        if not isinstance(denumenator, int):
            raise TypeError
        if denumenator == 0:
            raise ValueError

        self.numerator = numerator
        self.denumenator = denumenator

    def add_rational_with_same_numerator(self, numerator: int = 0, ) -> None:
        """
        Метод складывает рациональное число с другим, у которого одинаковый знаменатель.
        :param numerator: Числитель второго рационального числа.
        >>> r = Rational(2, 10)
        >>> r.add_rational_with_same_numerator(15)
        """
        if not isinstance(numerator, int):
            raise TypeError
        self.numerator += numerator

    def print(self) -> None:
        """ Метод выводит значение рационального числа в консоль."""
        print(f'Rational {self.numerator}/{self.denumenator}')


class Animal:
    def __init__(self,  sound: str, legs: int = 2):
        """Инициализация экземпляра класса.
           :param sound: "Голос" животного
           :param legs: Количество ног
         """
        if not isinstance(legs, int):
            raise TypeError
        if legs < 0:
            raise ValueError

        if not isinstance(sound, str):
            raise TypeError

        self.legs = legs
        self.sound = sound

    def voice(self) -> None:
        """ Метод выводит звук, который издает животное в консоль.
        >>> cat = Animal("Meu", 4)
        >>> cat.voice()
        """
        pass

    def grow(self) -> None:
        """ Метод выводит выводит информацию, что животное выросло в консоль."""
        print(f'{self} happy to grow and said {self.sound} twice')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
