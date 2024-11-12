# Given tuple of tuples
original_tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))


total_sum = 0
total_count = 0


for sub_tuple in original_tuple:
    print(sub_tuple)
    for number in sub_tuple:
        total_sum += number
        total_count += 1


average = total_sum / total_count


print("Average value:", average)