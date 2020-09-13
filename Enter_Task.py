"""
Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу. Каталог должен поддерживать
возможность добавления и удаления книг, редактирования информации о книге, а также обладать персистентностью
(т.е. сохранять библиотеку в внешнем файле и подгружать обратно). Также необходимо оформить точку входа,
поддерживать поиск по различным параметрам и обеспечить интерфейс взаимодействия пользователя с библиотекой.

Для добавления нового произведения следует указывать его жанр (по флагу -st), автора (по флагу -au),
название произведения (по флагу -wo), год издания (по флагу -ye) и условие save
Для удаления из библиотеки указывается номер в библиотеке (по флагу -bk) и условие delete
Для поиска указывается ключевое слово (по флагу -key) и условие show

# book_list = {
#     1: {'style': 'Фантастика', 'author': "Желязны", 'work': "Девять принцев Амбера", 'year': "1970"},
#     2: {'style': 'Фантастика', 'author': "Желязны", 'work': "Ружья Авалона", 'year': "1972"},
#     3: {'style': 'Фантастика', 'author': "Желязны", 'work': "Знак Единорога", 'year': "1975"},
#     4: {'style': 'Фантастика', 'author': "Желязны", 'work': "Рука Оберона", 'year': "1976"},
#     5: {'style': 'Детектив', 'author': "Дойл", 'work': "Скандал в Богемии", 'year': "1982"},
#     6: {'style': 'Детектив', 'author': "Дойл", 'work': "Союз рыжих", 'year': "1982"}
# }

Пример запуска кода:
python3 Tasks/enter_task.py show
python3 Tasks/enter_task.py -key Дойл show
python3 Tasks/enter_task.py -st Фантастика -au Ефремов -wo 'Туманность Андромеды' -ye 1957 save
python3 Tasks/enter_task.py -st Фантастика -au Ефремов -wo 'Час Быка' -ye 1970 save
python3 Tasks/enter_task.py -bk 8 delete
"""
import argparse
import json

json_file = 'library'
list_book = ""


# Для создания исходной библиотеки
def js(book_list: str) -> None:
    with open(json_file, 'w', encoding="utf-8") as file:
        json.dump(book_list, file)


# Если json пуст, добавляем нулевой элемент
def if_empty_json(json_file: str) -> None:
    with open(json_file, "w") as file:
        json.dump({0: {'style': 'Style', 'author': 'Author', 'work': 'Work', 'year': 'Year'}}, file)


# Поиск по ключевому слову в библиотеке
def find_in_json_data(json_file: str, list_book: str) -> None:
    parser = create_parser()
    namespace = parser.parse_args()
    search_key_name = namespace.key_word

    flag = True
    with open(json_file, 'r') as file:
        template = json.load(file)
    for search_book_list in template:
        print_ = f"№: {search_book_list} / " \
                 f"{template[search_book_list]['style']} / " \
                 f"{template[search_book_list]['author']} / " \
                 f"{template[search_book_list]['work']} / " \
                 f"{template[search_book_list]['year']}"
        if search_key_name == None:
            print(print_)
            flag = False
        elif search_key_name in template[search_book_list]['style'] \
                or search_key_name in template[search_book_list]['work'] \
                or search_key_name in template[search_book_list]['author'] \
                or search_key_name in template[search_book_list]['year']:
            list_book += print_ + '\n'
            flag = False
    if flag:
        print_ = 'Данная книга отсутствует в библиотеке'
        print(print_)
    print(list_book)


# Добавление нового произвдения в библиотеку
def input_to_json_data(json_file: str) -> None:
    parser = create_parser()
    namespace = parser.parse_args()
    with open(json_file, 'r') as file:
        template = json.load(file)
    for i in range(1, len(template) + 2):
        if f'{i}' not in template:
            book_ = i
            break
    if namespace.style is None:
        namespace.style = "Неизвестно"
    if namespace.work is None:
        namespace.work = "Неизвестно"
    if namespace.author is None:
        namespace.author = "Неизвестно"
    if namespace.year is None:
        namespace.year = "Неизвестно"
    template[book_] = {'style': namespace.style,
                       'author': namespace.author,
                       'work': namespace.work,
                       'year': namespace.year}
    with open(json_file, 'w', encoding="utf-8") as file:
        json.dump(template, file)


# Удаление из библиотеки произведения под номером -bk number
def delete_from_json_data(json_file: str) -> None:
    parser = create_parser()
    namespace = parser.parse_args()
    with open(json_file, 'r') as file:
        template = json.load(file)
    template.pop(namespace.book, None)
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(template, file)


# @line_profile
# Скелет программы
def work_with_library(json_file: str) -> None:
    parser = create_parser()
    namespace = parser.parse_args()

    if namespace.command == 'show':
        try:
            find_in_json_data(json_file, list_book)
        except json.decoder.JSONDecodeError:
            print("Проверьте, есть ли в вашей библиотеке хоть что-то...")

    elif namespace.command == 'save':
        try:
            input_to_json_data(json_file)
        except FileNotFoundError:
            return None
        except json.decoder.JSONDecodeError:
            if_empty_json(json_file)
            input_to_json_data(json_file)

    elif namespace.command == 'delete':
        delete_from_json_data(json_file)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-key",
                        "--key_word",
                        type=str,
                        help="Ключевое слово для поиска произведения")

    parser.add_argument("-bk", "--book",
                        type=str,
                        help="Номер нового произведения")

    parser.add_argument("-st", "--style",
                        type=str,
                        help="Жанр нового произведения")

    parser.add_argument("-au", "--author",
                        type=str,
                        help="Автор нового произведения")

    parser.add_argument("-wo", "--work",
                        type=str,
                        help="Название нового произведения")

    parser.add_argument("-ye", "--year",
                        type=str,
                        help="Год нового произведения")

    subparsers = parser.add_subparsers(dest="command")

    create_show_subparser(subparsers)
    create_save_subparser(subparsers)
    create_delete_subparser(subparsers)

    return parser


def create_show_subparser(subparsers):
    show_parser = subparsers.add_parser('show', help="Режим вывода списка произведений в консоль")


def create_save_subparser(subparsers):
    save_parser = subparsers.add_parser('save', help="Режим добавления в библиотеку")


def create_delete_subparser(subparsers):
    delete_parser = subparsers.add_parser('delete', help="Режим удаления книги из библиотеки")

