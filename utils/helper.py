def print_help() -> None:
    print(
        "Список доступных команд:\n"
        "add_book <Название> <Автор> <Год>\n"
        "remove_book <id>\n"
        "find_book <Название/Автор/Год>\n"
        "change_status <id> <'в наличии'/'выдана'>\n"
        "print_books\n"
        "help\n"
        "save <Файл> - Сохранить библиотеку в файл\n"
        "load <Файл> - Загрузить библиотеку из файла\n"
        "exit - Выйти из программы\n"
    )
