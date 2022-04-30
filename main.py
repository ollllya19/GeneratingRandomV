import math
import random

# calculating discrete random variable
def getDRV(n, k, lamb):

    # array of actual frequencies
    fact_f = [0 for _ in range(n)]

    for i in range(k):
        u = random.random()
        i = 0
        p = math.exp(-lamb)
        r = p
        while u > r:
            p *= lamb / (i + 1)
            r += p
            i += 1
        fact_f[i] += 1

    # calculating theoretical frequencies
    p = [math.exp(-lamb) * (lamb ** i) / math.factorial(i) for i in range(n)]
    teor_f = [p[i] * k for i in range(n)]

    # calculating X2
    chi2_nabl = sum([((fact_f[i] - teor_f[i]) ** 2) / teor_f[i] for i in range(n)])
    crit_value = 7.8

    print(f"Фактические частоты: {fact_f}")
    print(f"Теоретические частоты: {teor_f}")

    print(f"Кхи квадрат: {chi2_nabl}")
    print(f"Критическое значение: {crit_value}\n")


# calculating continious random variable
def getCRV(n, k, lamb):

    # array of actual frequencies
    fact_f = [0 for _ in range(n)]

    # list of RV
    x_values = []
    for i in range(k):
        u = random.random()
        x = - math.log(1 - u) / lamb
        x_values.append(x)

    end = int(max(x_values)) + 1
    step = end / n

    # calculating actual frequencies
    for x in x_values:
        i = int(x / step)
        fact_f[i] += 1

    # calculating average value
    aver_arr = [fact_f[i] * (step/2) * i for i in range(n)]
    aver = sum(aver_arr) / k

    # calculating theoretical frequencies
    p = [math.exp(-lamb * step * i) - math.exp(-lamb * step * (i + 1)) for i in range(n)]
    teor_f = [p[i] * k for i in range(n)]

    # calculating X2
    chi2_nabl = sum([(fact_f[i] - teor_f[i]) ** 2 / teor_f[i] for i in range(n)])
    crit_value = 7.8

    print(f"Конец отрзека: {end}")
    print(f"Шаг: {step}")

    print(f"Среднее значенеи, полученное в ходе генерирования: {aver}")
    print(f"Оценка предполагаемого показательного распределения: {1 / aver}")
    print(f"Вероятности попадания X в каждый интервал: {p}")

    print(f"Фактические частоты: {fact_f}")
    print(f"Теоретические частоты: {teor_f}")

    print(f"Кхи квадрат: {chi2_nabl}")
    print(f"Критическое значение: {crit_value}\n")


if __name__ == '__main__':

    getCRV(6, 200, 0.5)
    getDRV(4, 200, 0.5)