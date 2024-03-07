def display_phonebook():
    with open("phon.txt", "r") as file:
        for line in file:
            print(line.strip())

def find_by_lastname(lastname):
    found = False
    with open("phon.txt", "r") as file:
        for line in file:
            if lastname.lower() in line.lower():
                print(line.strip())
                found = True
    if not found:
        print("Абонент с фамилией", lastname, "не найден")

def find_by_phone(phone):
    found = False
    with open("phon.txt", "r") as file:
        for line in file:
            if phone in line.split()[2]:
                print(line.strip())
                found = True
    if not found:
        print("Абонент с номером", phone, "не найден")

def add_contact():
    lastname = input("Введите фамилию: ")
    firstname = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание: ")
    with open("phon.txt", "a") as file:
        file.write(f"{lastname} {firstname} {phone} {description}\n")

def edit_contact():
    phonebook = []
    with open("phon.txt", "r") as file:
        for line in file:
            phonebook.append(line.strip().split())

    lastname = input("Введите фамилию абонента для редактирования: ")
    for contact in phonebook:
        if contact[0].lower() == lastname.lower():
            print("Данные абонента:", " ".join(contact))
            choice = input("Что вы хотите изменить? (фамилия/имя/телефон/описание): ")
            new_value = input("Введите новое значение: ")
            if choice.lower() == "фамилия":
                contact[0] = new_value
            elif choice.lower() == "имя":
                contact[1] = new_value
            elif choice.lower() == "телефон":
                contact[2] = new_value
            elif choice.lower() == "описание":
                contact[3] = new_value
            else:
                print("Неверный ввод")
            break
    else:
        print("Абонент с фамилией", lastname, "не найден")

    with open("phon.txt", "w") as file:
        for contact in phonebook:
            file.write(" ".join(contact) + "\n")

def save_phonebook():
    with open("phon.txt", "r") as file:
        data = file.read()
    with open("newphon.txt", "w") as file:
        file.write(data)
    print("Справочник успешно сохранен в файле newphon.txt")

def main():
    while True:
        print("\nМеню:")
        print("1. Отобразить весь справочник")
        print("2. Найти абонента по фамилии")
        print("3. Найти абонента по номеру телефона")
        print("4. Добавить абонента в справочник")
        print("5. Изменить данные абонента")
        print("6. Сохранить справочник в новом файле")
        print("7. Закончить работу (выход)")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_phonebook()
        elif choice == "2":
            lastname = input("Введите фамилию: ")
            find_by_lastname(lastname)
        elif choice == "3":
            phone = input("Введите номер телефона: ")
            find_by_phone(phone)
        elif choice == "4":
            add_contact()
        elif choice == "5":
            edit_contact()
        elif choice == "6":
            save_phonebook()
        elif choice == "7":
            print("Работа программы завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
