def delete(list_, index=None):
    if index is None or index == -1:
        list_result = list_[:-1]
    else:
        list_result = list_[:index] + list_[index+1:]
    return list_result


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
