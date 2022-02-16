#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from folder import add, list, help, select

if __name__ == '__main__':
    workers = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            workers.append(add.add())

        elif command == 'list':
            list.list(workers)

        elif command.startswith('select '):
            select.select(workers)

        elif command == 'help':
            workers.append(help.help())

        else:
            print(f"Неизвестная команда {command}")
