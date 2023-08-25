def Merge(dict_1, dict_2):
    result = dict_1 | dict_2
    return result

dict_1 = dict(input("Enter key and value: ").split() for i in range(3))
dict_2 = dict(input("Enter key and value: ").split() for j in range(3))
dict_3 = Merge(dict_1, dict_2)
print(dict_3)
#hello world





	