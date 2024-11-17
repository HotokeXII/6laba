#Лабораторная работа №6
#задание 1: защита данных пользователя
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        if len(new_password) < 6:
            print('Пароль слишком короткий! Он должен содержать не менее 6 символов.')
        else:
            self.__password = new_password
            print('Пароль успешно изменён.')
    def check_password(self, password):
        return self.__password == password

user = UserAccount('byblik', 'pypok123@gmail.com', 'bazar1234')
user.set_password('meme')
user.set_password('perdoleibus')
print(user.check_password('perdimonokl'))
print(user.check_password('perdoleibus'))

#задание 2: полифоризм и наследование
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        Vehicle.__init__(self, make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        base_info = Vehicle.get_info(self)
        return f'{base_info}, Тип топлива: {self.fuel_type}'

vehicle = Vehicle('Toyota', 'Camry 3.5')
print(vehicle.get_info())
car = Car('Toyota', 'Camry 3.5', 'ракетное топливо гептил')
print(car.get_info())
