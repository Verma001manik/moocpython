def add_numbers_to_list(numbers: list):
    if(len(numbers)%5 ==0):
        return 
    else:
        last_number = numbers[-1]
        new_number = last_number+1
        numbers.append(new_number)
        add_numbers_to_list(numbers)
numbers = [1,3,4]
add_numbers_to_list(numbers)
print(numbers)