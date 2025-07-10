

# my_list = []
# swapped = True

# no_of_element = int(input("How many elements do you want to sort?: "))

# for i in range(no_of_element):
#     val = float(input("Enter an element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(no_of_element - 1):
#         if my_list[i] > my_list[i+1]:
#             swapped = True
#             my_list[i], my_list[i+1] = my_list[i+1],my_list[i]

# print("sorted list: {}".format(my_list))
# print(f"sorted list: {my_list}")
# print(sorted(my_list, reverse=True))


list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

a = 2
b = a
a = 1
print(b)