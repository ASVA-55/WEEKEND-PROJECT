def is_three_digit(n):
    return 100 <= n <= 999


def get_three_digit_input(prompt):
    value = int(input(prompt))
    if not is_three_digit(value):
        raise ValueError(f"{value} is not a 3-digit number. Please enter a number between 100 and 999.")
    return value


def sum_three_values(a, b, c):
    return a + b + c


def main():
    a = get_three_digit_input("Enter first 3-digit number: ")
    b = get_three_digit_input("Enter second 3-digit number: ")
    c = get_three_digit_input("Enter third 3-digit number: ")
    result = sum_three_values(a, b, c)
    print(f"Sum: {result}")
    return result


if __name__ == "__main__":
    main()
