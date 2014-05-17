def binary_search(lst,target):
    lst.sort()
    begin = 0
    end = len(lst)-1
    while begin <= end:
        middle_of_list = (begin + end) // 2
        if lst[middle_of_list] == target: return "index: ", middle_of_list, "list: ", lst
        if target < lst[middle_of_list]:
            end = middle_of_list - 1
        else:
            begin = middle_of_list + 1
    return -1

print(binary_search([5,3,2,52,32],32))
