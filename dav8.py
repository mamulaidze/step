from concurrent.futures import ThreadPoolExecutor


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

with ThreadPoolExecutor() as executor:
    results = executor.map(is_prime, num_list)

for num, result in zip(num_list, results):
    print(num, "არის მარტივი:", result)