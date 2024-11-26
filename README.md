# Система управления библиотекой
## 📋 Команды:
- ```add_book <Название> <Автор> <Год>``` - добавляет книгу в библиотеку
- - ```add_book "Война и мир" 'Лев Толстой' 1869```
- ```remove_book <id>``` - удаляет книгу по индексу
- - ```remove_book 1```
- ```find_book <Название/Автор/Год>``` - находит все книги с заданным именем
- - ```find_book 'Война и мир'```
- - ```find_book "Лев Толстой"```
- - ```find_book 1869```
- ```change_status <id>``` <'в наличии'/'выдана'> - изменяет статус книги
- - ```change_status 1 "в наличии"```
- - ```change_status 1 выдана```
- ```print_books``` - выводит все книги из библиотеки
- ```help``` - выводит список всех доступных команд с краткими пояснениями
- ```save <Файл>``` - сохраняет библиотеку в файл в формате **JSON**
- - ```save library.json```
- ```load <Файл>``` - загружает библиотеку из файла в формате **JSON**
- - ```load library.json```
- ```exit``` - завершает работу программы
## 📋 Примечания:
- Для передачи длинных аргументов таких как ```'в наличии'``` или ```"Иван Петров"```, используйте кавычки
- - Одинарные ```'```
- - Двойные ```"```
- ```id``` и ```year``` необходимо указывать в числовом формате
- Формат файлов для сохранения/загрузки библиотеки — **JSON**
- Методы класса ```Library``` возвращают результат в виде итогового сообщения для пользователя