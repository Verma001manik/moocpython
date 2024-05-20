import math
def square_roots(numbers: list):
    sq_roots = [math.sqrt(number) for number in numbers]
    return sq_roots
lines = square_roots([1,2,3,4])
for line in lines:
    print(line)