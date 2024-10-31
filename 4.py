def gcdex(a, b):
    # Ініціалізація змінних для розширеного алгоритму Евкліда
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def inverse_element_2(a, n):
    # Перевірка на простоту числа n
    if is_prime(n):
        # Використання малої теореми Ферма для оберненого елемента, якщо n - просте
        return pow(a, n - 2, n)
    else:
        # Використання теореми Ейлера для обчислення мультиплікативного оберненого
        def phi(m):
            result = m
            p = 2
            while p * p <= m:
                if m % p == 0:
                    while m % p == 0:
                        m //= p
                    result -= result // p
                p += 1
            if m > 1:
                result -= result // m
            return result

        # Перевірка взаємної простоти чисел a і n
        if gcdex(a, n)[0] == 1:
            phi_n = phi(n)
            return pow(a, phi_n - 1, n)
        else:
            return None

# Приклад для перевірки
a = 5
n = 18
print(f"Мультиплікативний обернений елемент для {a} по модулю {n}: {inverse_element_2(a, n)}")
