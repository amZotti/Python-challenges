def search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
    raise Exception("Target not found")
