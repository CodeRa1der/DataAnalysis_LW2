#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def add_route():
    # Запись данных маршрута
    first = input('Первая точка маршрута: ')
    second = input('Вторая точка маршрута: ')
    # Создание словаря
    return {
        'first': first,
        'second': second,
    }

def export_to_json(file, routes_list):
    with open(file, 'w', encoding='utf-8') as fileout:
        json.dump(routes_list, fileout, ensure_ascii=False, indent=4)


def import_json(file):
    with open(file, 'r', encoding='utf-8') as filein:
        return json.load(filein)

def list_of_routes(roadway):
    if roadway:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 14,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^5} | {:^20} | {:^20} |'.format(
               "Номер маршрута",
                "Место отправки",
                "Место прибытия"
            )
        )
        print(line)
        # Вывод данных о маршрутах
        for number, route in enumerate(roadway, 1):
            print(
                '| {:<14} | {:<20} | {:<20} |'.format(
                    number,
                    route.get('first', ''),
                    route.get('second', '')
                )
            )
            print(line)
    else:
        print("Список маршрутов пуст")


def help():
    print('\nСписок команд:')
    print('help - Вывести этот список')
    print('add - Добавить маршрут')
    print('list - Показать список маршрутов')
    print('exit - Выйти из программы')
    print('export - Экспортировать данные в JSON-файл')
    print('import (имя файла) - Импортировать данные')


def main():
    # Список маршрутов
    routes = []
    # Начало бесконечного цикла команд
    while True:
        # Сюда вписывать команды
        command = input('>>> ').lower()

        # Команда help
        if command == 'help':
            help()

        # Команда add
        elif command == 'add':
            route = add_route()
            # Добавление словаря в список
            routes.append(route)

        # Команда list
        elif command == 'list':
            list_of_routes(routes)

        elif command == 'export':
            export_to_json('individual.json', routes)

        elif command.startswith('import '):
            parts = command.split(maxsplit=1)
            file = parts[1]
            routes = import_json(file)

        # Команда exit
        elif command == 'exit':
            break

        # Другая команда/неверно введенная команда
        else:
            print(f'Неизвестная команда {command}')


if __name__ == '__main__':
    main()
