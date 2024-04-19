# Средний уровень:
# 1) Разработайте класс BankAccount, который имеет атрибуты balance (баланс) и owner (владелец).
# Реализуйте методы deposit(amount) для внесения средств на счет и withdraw(amount) для снятия средств со счета.
# Учтите возможность проверки наличия достаточного баланса перед снятием.
# from decimal import Decimal
# class BankAccount:
#     def __init__(self, balance: Decimal, owner: str):
#         self.balance = balance
#         self.owner = owner
#
#     def deposit(self, amount: Decimal):
#         self.balance += amount
#         return f'{self.owner}: Ваш баланс поповнено на {amount}'
#
#     def withdraw(self, amount: Decimal):
#         if self.balance >= amount:
#             self.balance -= amount
#             return f'{self.owner}: З вашого балансу знято {amount}'
#         return f'{self.owner}: Недостатній баланс'
#
#
# acc1 = BankAccount(balance=Decimal("40"), owner="gudzik")
# acc2 = BankAccount(balance=Decimal("10"), owner="ivan")
# acc3 = BankAccount(balance=Decimal("0"), owner="antena")
# acc4 = BankAccount(balance=Decimal("200"), owner="kum")
# print(acc1.deposit(Decimal("30")))
# print(acc1.balance)
# print(acc2.deposit(Decimal("100")))
# print(acc2.balance)
# print(acc3.withdraw(Decimal("90")))
# print(acc3.balance)
# print(acc4.withdraw(Decimal("200")))
# print(acc4.balance)

# 2) Создайте класс Library, представляющий библиотеку.
# Класс должен иметь атрибуты books (список книг) и members (список членов библиотеки).
# Реализуйте методы add_book(book) для добавления книги в библиотеку,
# remove_book(book) для удаления книги из библиотеки,
# add_member(member) для добавления нового члена библиотеки и
# remove_member(member) для удаления члена библиотеки.
# Также реализуйте метод checkout_book(book, member) для выдачи книги члену библиотеки и
# return_book(book, member) для возврата книги в библиотеку.

# class Library:
#     def __init__(self, books: list, members: list):
#         self.books = books
#         self.members = members
#         self.members_books_dict = {}
#
#     def add_book(self, book):
#         self.books.append(book)
#         return f' Книгу {book} додано в бібліотеку'
#
#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#         return f' Книгу {book} видалено з бібліотеки'
#
#     def add_member(self, member):
#         self.members.append(member)
#         return f'Учасника {member} додано до списку членів бібліотеки'
#
#     def remove_member(self, member):
#         if member in self.members:
#             self.members.remove(member)
#         return f'Учасника {member} видалено зі списку членів бібліотеки'
#
#     def checkout_book(self, book, member):
#         if member not in self.members:
#             print(f'{member} не є учасником клубу')
#             return
#
#         if book not in self.books:
#             print(f'Книги {book} немає в наявності')
#             return
#
#         if member not in self.members_books_dict:
#             self.members_books_dict[member] = [book]
#         else:
#             self.members_books_dict[member].append(book)
#
#         self.remove_book(book)
#         print(f'Користувач {member} взяв книжку {book}')
#
#     def return_book(self, book, member):
#         if member not in self.members_books_dict or book not in self.members_books_dict[member]:
#             print(f"Користувач {member} не брав книгу {book}")
#             return
#
#         self.members_books_dict[member].remove(book)
#
#         self.add_book(book)
#         print(f"Користувач {member} повернув книгу {book}")
#
# Library1 = Library(books=[], members=[])
# Library1.add_book("Володар перснів")
# Library1.add_book("Трансерфінг реальності")
# Library1.add_book("Колобок")
# Library1.add_book("Абетка")
# print(Library1.books)
# Library1.remove_book("Колобок")
# print(Library1.books)
# Library1.add_member("Антена")
# Library1.add_member('Швагро')
# print(Library1.members)
# Library1.remove_member("Антена")
# print(Library1.members)
#
# Library1.checkout_book(book="Володар перснів", member="Швагро")
#
# Library1.return_book(book="Володар перснів", member="Швагро")
#
# Library1.return_book(book="Абетка", member="Швагро")














