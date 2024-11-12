# Original tuples
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)


elementwise_sum = []


for i in range(len(tuple1)):
    print(i)
    sum_value = tuple1[i] + tuple2[i] + tuple3[i]
    elementwise_sum.append(sum_value)


elementwise_sum = tuple(elementwise_sum)


print("Element-wise sum of given tuples:", elementwise_sum)
