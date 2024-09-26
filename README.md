# Calculate Expression

Функция `calculate_expression` принимает строку, представляющую арифметическое выражение, содержащее только знаки `+` и `-`, и возвращает результат этого выражения. Функция обрабатывает как однозначные, так и многозначные числа.

## Пример

```Python
# Примеры использования
try:
    print(calculate_expression("1+2+3+4"))      # Вывод: 10
    print(calculate_expression("10-2+3-4"))     # Вывод: 7
    print(calculate_expression("15+25-10+5"))   # Вывод: 35
    print(calculate_expression("100-50+25-75")) # Вывод: 0
    print(calculate_expression("10+2a-3"))      # Вывод: ValueError
except ValueError as e:
    print(f"Ошибка: {e}")
```

## Сборка Docker-образа

Открыть терминал, перейти в каталог проекта и выполнить следующую команду для сборки Docker-образа:

```bash
docker build -t calculate_expression_app .
```

## Запуск контейнера

После успешной сборки образа для запуска контейнера введите следующую команду:

```bash
docker run --rm calculate_expression_app
```

## Дополнение 

Для того, чтобы контейнер запускал программу (функцию calculate_expression), а не только тесты, необходимо изменить команду CMD в Dockerfile на:

```dockerfile
CMD ["python", "main.py"]
```
