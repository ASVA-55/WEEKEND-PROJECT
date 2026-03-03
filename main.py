def isdigit(n):
    return 100 <= n <= 999


def get_input(prompt):
    value = int(input(prompt))
    if not isdigit(value):
        raise ValueError(f"{value} is not a 3-digit number. Please enter a number between 100 and 999.")
    return value


def sum(a, b, c):
    return a+b+c


def main():
    a = get_input("Enter first 3-digit number: ")
    b = get_input("Enter second 3-digit number: ")
    c = get_input("Enter third 3-digit number: ")
    result = sum(a, b, c)
    print(f"Sum: {result}")
    return result


if __name__ == "__main__":
    main()
