import math


numbers = [45, 67, 90, 4, 12]


print("Square Roots:")
for num in numbers:
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root}")


print("\nCubed Values:")
index = 0
while index < len(numbers):
    cubed_value = numbers[index] ** 3
    print(f"The cubed value of {numbers[index]} is {cubed_value}")
    index += 1
