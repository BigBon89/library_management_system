from library.library import Library
from utils.commands import Command, command_handler


def main():
    library = Library()
    print("Введите 'help' для получения списка команд")
    while True:
        input_line = input().strip()

        if not input_line:
            print("Введите команду")
            continue

        command_object = Command(input_line)

        if command_object.command.lower() == "exit":
            break

        command_handler(command_object, library)


if __name__ == '__main__':
    main()
