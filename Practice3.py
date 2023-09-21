def sum_digits(number):
    digit_sum = 0
    
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    
    return digit_sum
number = 123456789
result = sum_digits(number)
print(f"Сумма цифр числа {number} равна {result}")