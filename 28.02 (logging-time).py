import time

def measure(func):
    start = time.time()
    func()
    end = time.time()
    length = end - start
    return length

def test():
    time.sleep(0.5)

time = measure(test)

print("Час виконання:", time)

if time >= 0.5:
    print("Все працює правильно!")
else:
    print("Помилка!")


