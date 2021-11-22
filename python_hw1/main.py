my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# print(my_list)
sorted_list = sorted(my_list)
sorted_inv_list = sorted(my_list, reverse=True)
print(my_list)
print(sorted_list)
print(sorted_inv_list)

even_list = my_list[::2]
odd_list = my_list[1::2]
print(even_list)
print(odd_list)

multiple_of_3 = []
for item in my_list:
    if item % 3 == 0:
        multiple_of_3.append(item)

print(multiple_of_3)
