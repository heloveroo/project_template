def output_to_console(text):
    """
    Функція для виводу тексту у консоль

    Аргументи:
        text (str): Текст для виводу
    """
    print(text)


def write_to_file_builtin(filename, content):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python

    Аргументи:
        filename (str): Шлях до файлу
        content (str): Вміст для запису
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)