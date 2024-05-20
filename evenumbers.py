def even_numbers(beginning: int, maximum: int):
    for i in range (beginning, maximum+1):
        if i%2==0:
            yield i 
    
numbers = even_numbers(2, 10)
for number in numbers:
    print(number)

numbers = even_numbers(11, 21)
for number in numbers:
    print(number)