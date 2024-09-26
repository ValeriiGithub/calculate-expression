from functools import lru_cache


@lru_cache(maxsize=None)  # Неограниченный размер кэша
def calculate_expression(expression: str) -> int:
    # Проверка на некорректные данные
    if not expression or expression[0] in '+-' or expression[-1] in '+-':
        raise ValueError("Входная строка должна содержать только цифры, знаки '+' и '-'.")

    if any(expression[i] in '+-' and expression[i + 1] in '+-' for i in range(len(expression) - 1)):
        raise ValueError("Входная строка должна содержать только цифры, знаки '+' и '-'.")

    if not all(char.isdigit() or char in '+-' for char in expression):
        raise ValueError("Входная строка должна содержать только цифры, знаки '+' и '-'.")

    result = 0
    current_number = 0
    sign = 1  # 1 для '+', -1 для '-'

    for char in expression:
        if char.isdigit():
            # Формируем текущее число
            current_number = current_number * 10 + int(char)
        elif char in '+-':
            # Добавляем текущее число к результату с учетом знака
            result += sign * current_number
            current_number = 0  # Сбрасываем текущее число

            # Обновляем знак
            if char == '+':
                sign = 1
            else:  # char == '-'
                sign = -1

    # Добавляем последнее число к результату
    result += sign * current_number
    return result


# Примеры использования
try:
    print(calculate_expression("1+2+3+4"))      # Вывод: 10
    print(calculate_expression("10-2+3-4"))     # Вывод: 7
    print(calculate_expression("15+25-10+5"))   # Вывод: 35
    print(calculate_expression("100-50+25-75")) # Вывод: 0
    print(calculate_expression("10+2a-3"))      # Вывод: ValueError
except ValueError as e:
    print(f"Ошибка: {e}")
