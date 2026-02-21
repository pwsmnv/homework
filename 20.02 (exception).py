result = []

def divider(a, b):
    if a < b:
        raise ValueError("значение делимого меньше значения делителя")
    if b > 100:
        raise IndexError("значение делителя больше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 90: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except TypeError:
        print("Ошибка: введите число")
    except (ValueError,IndexError) as e:
        print("Ошибка:", e)

print(result)