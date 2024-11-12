def have_common_member(list1, list2):

    for item in list1:
        if item in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

result = have_common_member(list1, list2)
print(result)  

list3 = [10, 20, 30]
list4 = [40, 50, 60]

result2 = have_common_member(list3, list4)
print(result2)  