def remove_smaller_than(numbers : list, limit: int):
    result = [print(number) for number in numbers if number>= limit]

numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))