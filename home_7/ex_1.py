first_list = [1, 2, 3, 4, 5, 7, 8, 9, 6]
second_list = [1, 12, 4, 14, 6, 16]
print(f'Count numbers in first n second list: {len(set(first_list) & set(second_list))}')
