def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Division by zero not allowed"


def modules(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result %= num
    return result


def power(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result **= num
    return result


def floor_division(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result //= num
    return result


while True:
    print("\n--- Calculator Menu ---")
    print("Options: add | subtract | multiply | divide | mod | power | floor")
    print("Type 'exit' to quit.")

    do = input("Enter your choice: ").lower()

    if do == "exit":
        print("Calculator exiting... Goodbye! 👋")
        break

    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    if do == "add":
        print("Result:", add(numbers))
    elif do == "subtract":
        print("Result:", subtract(numbers))
    elif do == "multiply":
        print("Result:", multiply(numbers))
    elif do == "divide":
        print("Result:", divide(numbers))
    elif do == "mod":
        print("Result:", modules(numbers))
    elif do == "power":
        print("Result:", power(numbers))
    elif do == "floor":
        print("Result:", floor_division(numbers))
    else:
        print("Invalid choice. Try again!")
