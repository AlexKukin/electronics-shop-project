import csv
import os.path
from config import ROOT_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""
        Item.all = []
        file_path = os.path.join(ROOT_PATH, file_path)

        items = []
        with open(file_path, newline='', encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                items.append(Item(name, price, quantity))

    @staticmethod
    def string_to_number(str_num: str) -> int:
        """Возвращает целую часть число из числа-строки"""
        return int(float(str_num))

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
