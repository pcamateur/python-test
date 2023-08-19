import time


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence


start_time = time.time()
fib_numbers = fibonacci(5000)
print(fib_numbers)
end_time = time.time()
execution_time = end_time - start_time
print("代码运行时间: ", execution_time, "秒")


def fibonacci1(n1):
    if n1 <= 1:
        return n1
    else:
        return fibonacci1(n1 - 1) + fibonacci1(n1 - 2)


start_time1 = time.time()

n1 = 30
fib_numbers1 = [fibonacci1(i) for i in range(n1)]
print(fib_numbers1)

end_time1 = time.time()
execution_time1 = end_time1 - start_time1
print("代码运行时间: ", execution_time1, "秒")


def fibonacci2(n2):
    if n2 <= 1:
        return n2
    else:
        prev = 0
        curr = 1
        for _ in range(2, n2 + 1):
            next_number = prev + curr
            prev, curr = curr, next_number
        return curr


start_time2 = time.time()
n2 = 300
fib_numbers2 = [fibonacci2(i) for i in range(n2)]
print(fib_numbers2)
end_time2 = time.time()
execution_time2 = end_time2 - start_time2
print("代码运行时间: ", execution_time2, "秒")


