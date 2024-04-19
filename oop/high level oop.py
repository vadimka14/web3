# Сложный уровень:
# 1) Создайте систему регистрации на конференцию.
# Реализуйте классы Conference (конференция), Participant (участник) и
# RegistrationSystem (система регистрации).
# Класс Conference должен иметь атрибуты name (название) и capacity (вместимость),
# класс Participant - атрибуты name (имя) и email (электронная почта),
# а класс RegistrationSystem - атрибуты conference (конференция) и participants (список участников),
# а также методы register(participant) для регистрации участника и
# is_registration_available() для проверки доступности регистрации на конференцию.
# Реализуйте проверку наличия свободных мест на конференции перед регистрацией.


# class Conference:
#     def __init__(self, name: str, capacity: int):
#         self.name = name
#         self.capacity = capacity
#
#
#
#
#
# class Participant:
#     def __init__(self, name: str, email: str):
#         self.name = name
#         self.email = email
#
#
#
#
#
# class RegistrationSystem:
#     def __init__(self, conference: Conference, participants: list[Participant]):
#         self.conference = conference
#         self.participants = participants
#
#     def register(self, participant: Participant):
#         if len(self.participants) >= self.conference.capacity:
#             print(f"На конференцію {self.conference.name} немає вільних місць")
#             return
#
#         if participant in self.participants:
#             print(f'Гість {participant} вже зареєстрований на конференцію {self.conference.name}')
#
#         self.participants.append(participant)
#         print(f"Гостя {participant.name} зареєстровано на конференцію {self.conference.name}")
#
#
#     def is_registration_available(self, participant: Participant):
#         if participant in self.participants:
#             return True
#         return False
#
#
# conference1 = Conference(name="Ethereum", capacity=4)
# p1 = Participant(name="John", email='aue@gmail.com')
# p2 = Participant(name="Andrew", email='antena@gmail.com')
# p3 = Participant(name="Antony", email='antena@gmail.com')
# p4 = Participant(name="Artur", email='antena@gmail.com')
# p5 = Participant(name="Bill", email='antena@gmail.com')
#
# rs = RegistrationSystem(conference=conference1, participants=[p1, p2, p3])
#
# rs.is_registration_available(participant=p4)
#
# rs.register(participant=p4)
# rs.register(participant=p5)



# 2) Создайте игру "Магазин животных".
# Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена),
# а также методом sound(), который возвращает звук, издаваемый животным.
# От него унаследуйте классы Dog, Cat и Bird,
# каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.
# Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина),
# а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного.
# Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.


class Animal:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def sound(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'



class Dog(Animal):
    def sound(self):
        print("гав")


class Cat(Animal):
    def sound(self):
        print("мяу")

class Bird(Animal):
    def sound(self):
        print("чірік")



class Shop:
    def __init__(self, animals: list, budget: float):
        self.animals = animals
        self.budget = budget

    def buy_animal(self, animal: Animal):
        if animal.price > self.budget:
            print(f"Недостатньо коштів для покупки {animal.name}")
            return
        self.animals.append(animal)
        self.budget -= animal.price
        print(f"В магазині новий гість - {animal.name}")


    def sell_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.budget += animal.price
            print(f"Ось ваш улюбленець на ім'я {animal.name}")
        else:
            print(f"На жаль, {animal.name} вже знайшов свого господаря")
bird1 = Bird(name="ptenchik", price=10_000)
cat1 = Cat(name='merci', price=100_000)
dog1 = Dog(name='barsik', price=10_100_500)

shop = Shop(animals=[bird1], budget=200_000)


# bird1.sound()
# cat1.sound()
# dog1.sound()
print(shop.budget)
shop.buy_animal(animal=cat1)
print(shop.budget)
shop.buy_animal(animal=dog1)

shop.sell_animal(animal=bird1)
shop.sell_animal(animal=dog1)
print(shop.animals)