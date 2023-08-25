def get_even_numbers(input_list):
    even_numbers = []
    
    for number in input_list:
        squarenum = number*number
        if (squarenum) % 2 == 0:
            even_numbers.append(squarenum)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
