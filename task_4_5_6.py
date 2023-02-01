"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        pass


class OfficeEquipment:
    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.number = number_of_lists
        try:
            if isinstance(quantity, int):

                self.quantity = quantity

                self.my_unit = {
                    'Модель устройства': self.name,
                    'Цена за ед.': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise MyOwnExc("Вы ввели не число!!!")

        except MyOwnExc as e:
            print(e.txt)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'Принтеров {self.number} '


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'Сканеров {self.number} '


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'Ксероксов  {self.number} '


unit1 = Printer('Aser', 3102, 6, 9)
unit2 = Scanner('Samsung', 1840, 4, 15)

Warehouse.reception(unit1)
Warehouse.reception(unit2)

print(Warehouse.goods)
print(unit2.to_scan())
