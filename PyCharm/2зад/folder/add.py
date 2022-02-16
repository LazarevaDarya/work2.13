def add():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    number = int(input("Номер телефона: "))
    date_obj = input("Дата рождения: ").split('.')
    workers = {
        'surname': surname,
        'name': name,
        'number': number,
        'date_obj': date_obj,
    }
    return workers

