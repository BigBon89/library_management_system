import re
from inspect import ismethod

from library.library import Library
from utils.helper import print_help


class Command:
    def __init__(self, command: str):
        pattern = r'([\'\"].+?[\'\"])|(\S+)'
        matches = re.findall(pattern, command)

        self._command = ""

        if matches:
            self._command = matches[0][1]
        self._args = [match[0].strip('\"\'') or match[1] for match in matches[1:]]

    @property
    def command(self) -> str:
        return self._command

    @property
    def args(self) -> list:
        return self._args


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

    expected_args = command_map[command_object.command].__code__.co_argcount
    if ismethod(command_map[command_object.command]):
        expected_args -= 1

    if len(command_object.args) != expected_args:
        print(f"Команда '{command_object.command}' "
              f"ожидает {expected_args} аргументов, получено {len(command_object.args)}")
        return

    print(command_map[command_object.command](*command_object.args))