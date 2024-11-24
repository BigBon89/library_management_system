from inspect import ismethod

from library.library import Library
from utils.helper import print_help
from utils.commands import Command


def command_handler(command_object: Command, library: Library) -> None:
    """Обрабатывает команды"""

    command_map = {
        "add_book": library.add_book,
        "remove_book": library.remove_book,
        "find_book": library.find_book,
        "change_status": library.change_status,
        "print_books": lambda: print(library),
        "help": print_help,
        "save": library.save_to_file,
        "load": library.load_from_file,
    }

    if command_object.command not in command_map:
        print("Неизвестная команда. Используйте 'help' для справки")
        return

    if ismethod(command_map[command_object.command]):
        expected_args = command_map[command_object.command].__code__.co_argcount - 1
    else:
        expected_args = command_map[command_object.command].__code__.co_argcount

    if len(command_object.args) != expected_args:
        print(f"Команда '{command_object.command}' "
              f"ожидает {expected_args} аргументов, получено {len(command_object.args)}.")
        return

    if command_object.args:
        command_map[command_object.command](*command_object.args)
    else:
        command_map[command_object.command]()


def main():
    library = Library()


if __name__ == '__main__':
    main()
