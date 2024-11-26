def print_help() -> None:
    """Выводит справочную информацию"""

    print(
        "Для передачи длинных аргументов таких как 'в наличии' или \"Иван Петров\", используйте \' или \"\n"
        "Список доступных команд:\n"
        "add_book <Название> <Автор> <Год> - добавляет книгу в библиотеку\n"
        "remove_book <id> - удаляет книгу из библиотеки\n"
        "find_book <Название/Автор/Год> - находит все книги с заданным именем\n"
        "change_status <id> <'в наличии'/'выдана'> - изменяет статус книги\n"
        "print_books - выводит все книги из библиотеки\n"
        "help - выводит список всех доступных команд с краткими пояснениями\n"
        "save <Файл> - сохраняет библиотеку в файл\n"
        "load <Файл> - загружает библиотеку из файла\n"
        "exit - завершает работу программы\n"
    )
