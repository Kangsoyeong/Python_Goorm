num_list = [1, 9, 2, 3, 4, 5, 7]

num_list.sort()
print(num_list)

num_list.remove(9)
print(num_list)

num_list.insert(num_list.index(5) + 1, 6)
print(num_list)

num_list.append(8)
print(num_list)

num_list.sort(reverse=True)
print(num_list)