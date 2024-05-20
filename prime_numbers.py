def prime_numbers():
    number = 2
    yield number
    
   

numbers = prime_numbers()
for i in range(8):
    print(next(numbers))