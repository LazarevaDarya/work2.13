def select(workers):
    surname = input("Введите фамилию: ")
    for elem in workers:
        if elem['surname'] == surname:
            print(f"Имя: {str(elem['name'])}\nНомер телефона: {str(elem['number'])}\n"
                  f"Дата рождения: {elem['date_obj']}")
            return
        else:
            print("Фамилии не найдено")
