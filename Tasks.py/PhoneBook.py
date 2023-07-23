
contacts = {}

# Функция для добавления нового контакта
def add_contact():
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    contacts[name] = phone
    print("Контакт успешно добавлен")

# Функция для поиска контакта по имени
def find_contact():
    name = input("Введите имя контакта: ")
    if name in contacts:
        print("Номер телефона контакта {}: {}".format(name, contacts[name]))
    else:
        print("Контакт не найден")

# Функция для вывода всех контактов
def show_contacts():
    if len(contacts) == 0:
        print("Список контактов пуст")
    else:
        for name, phone in contacts.items():
            print("{}: {}".format(name, phone))

# Основной цикл программы
while True:
    # Выводим меню
    print("\nТелефонный справочник")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Показать все контакты")
    print("4. Выход")

    # Ждем ввода пользователя
    choice = input("Выберите действие: ")

    # Обрабатываем выбор пользователя
    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        show_contacts()
    elif choice == "4":
        break
    else:
        print("Неверный выбор")






