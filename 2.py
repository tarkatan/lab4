def gcdex(a, b):
    # Ініціалізація змінних для розширеного алгоритму Евкліда
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def inverse_element(a, n):
    d, x, _ = gcdex(a, n)
    # Оборотний елемент існує тільки тоді, коли gcd(a, n) = 1
    if d == 1:
        return x % n  # результат у межах модуля n
    else:
        return None  # немає оберненого елемента, якщо gcd не 1

# Приклад перевірки
a = 5
n = 18
inverse = inverse_element(a, n)
if inverse is not None:
    print(f"Мультиплікативний обернений елемент для {a} по модулю {n}: {inverse}")
else:
    print(f"Мультиплікативного оберненого елемента для {a} по модулю {n} не існує")
