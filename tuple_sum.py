def tuple_sum():
    # Takes a tuple of integers using user input
    t= input("Enter integers separated with a single space: ")
    my_tuple = tuple(int(item) for item in t.split())

    print(my_tuple)
    #adds all input together
    result= sum(my_tuple)
    print("The sum of the list is" ,result)

tuple_sum()