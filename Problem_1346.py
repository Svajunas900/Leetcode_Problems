
def checkIfExist(arr):
    a_dict = {}
    for index, value in enumerate(arr):
        if value * 2 in a_dict and a_dict[value*2] != index:
            return True
        elif value / 2 in a_dict and a_dict[value / 2] != index:
            return True
        else:
            a_dict[value] = index
    return False
