from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin
import os

def main():
    """
        Головна функція, яка виконує:
        1. Введення тексту з консолі
        2. Читання з файлу (вбудованими засобами та через pandas)
        3. Вивід результатів у консоль
        4. Запис результатів у файл
        """
    # Створюємо папки data та output, якщо їх немає
    os.makedirs('data', exist_ok=True)
    os.makedirs('output', exist_ok=True)

    
    console_text = input_from_console()    # 1. Введення з консолі
    output_to_console(f"Текст з консолі: {console_text}")
    write_to_file_builtin("output/console_output.txt", f"Текст з консолі: {console_text}")

    try:    # 2. Читання з файлу
        file_content = read_from_file_builtin("data/input.txt")
        output_to_console(f"Вміст файлу (вбудований спосіб):\n{file_content}")
        write_to_file_builtin("output/file_output_builtin.txt", f"Вміст файлу:\n{file_content}")
    except FileNotFoundError:
        output_to_console("Помилка: файл input.txt не знайдено")

    try:   # 3. Читання з файлу (pandas)
        pandas_data = read_from_file_pandas("data/data.csv")
        output_to_console(f"Дані з файлу (pandas):\n{pandas_data}")
        write_to_file_builtin("output/file_output_pandas.txt", f"Дані з файлу:\n{pandas_data.to_string()}")
    except Exception as e:
        output_to_console(f"Помилка при читанні через pandas: {str(e)}")


if __name__ == '__main__':
    main()