def list(workers):
    for num, elem in enumerate(workers):
        print(f"{num + 1}.\n{str(elem['surname'])} {str(elem['name'])}\n"
              f"Номер телефона: {str(elem['number'])}\n Дата рождения: {elem['date_obj']}")

