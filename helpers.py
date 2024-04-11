
import re


def validate_cpf(cpf: str) -> bool:
    # Remove punctuation from the CPF string
    cpf = re.sub(r'\D', '', cpf)

    # verify if the CPF has 11 digits
    if len(cpf) != 11:
        return False

    # Convert the CPF string to a list of integers
    numbers = [int(digit) for digit in cpf]

    # Check if all digits are the same
    if len(set(numbers)) == 1:
        return False

    # Check the first verification digit
    sum_of_products = sum(a * b for a, b in zip(numbers[:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Check the second verification digit
    sum_of_products = sum(a * b for a, b in zip(numbers[:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True