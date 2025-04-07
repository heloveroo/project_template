def input_from_console():
    """
    Функція для вводу тексту з консолі.
    Повертає:
        str: Текст, введений користувачем.
    """
    return input("Введіть текст: ")


def read_from_file_builtin(filename):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.
    Повертає:
        str: Вміст файлу у вигляді рядка.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_pandas(filename):
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas.
    Повертає:
        pandas.DataFrame: Дані з файлу у вигляді таблиці (DataFrame).
    """
    import pandas as pd
    return pd.read_csv(filename)