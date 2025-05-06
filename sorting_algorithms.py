# Bubble sort

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j+1]
                my_list[j+1] = my_list[j]
                my_list[j] = temp
    return my_list


def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def _merge(list_1, list_2):
    i = 0
    j = 0
    combined = []
    # print(list_1, list_2)
    while len(list_1) > i and len(list_2) > j:
        if list_1[i] < list_2[j]:
            combined.append(list_1[i])
            i += 1
        else:
            combined.append(list_2[j])
            j += 1
    # print(list_2, list_1)
    # while len(list_1) > i:
    #     combined.append(list_1[i])
    #     i += 1
    # while len(list_2) > j:
    #     combined.append(list_1[j])
    #     j += 1
    # print(combined)
    return combined


def merge_sort(my_list):

    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return _merge(left, right)


print(bubble_sort([4, 2, 6, 5, 1, 3]))
print(selection_sort([4, 2, 6, 5, 1, 3]))
print(merge_sort([4, 2, 6, 5, 1, 3]))
