def apply_all_func(int_list, *functions):         # Создаем функцию
    results = {}                                  # Создаем пустой словарь
    for i in functions:                           # Перебераем функции в списке функций functions
        results[i.__name__] = str(i(int_list))    # Добавляем в список значение, где ключ - имя функции,
                                                  # а значение - результат функции
    return results                                # Возвращаем словарь в консоль

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))