import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(list, quantity=1):
    for _ in range(quantity):
        number = random.uniform(1, 100)
        rounded = round(number, 1)
        list.append(rounded)

if __name__ == "__main__":
    main()