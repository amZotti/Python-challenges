#selection sort
lst = [1,5,3,1,4]

def sort(lst):
    for i in range(len(lst)-1):
        current = i
        for j in range(i + 1, len(lst):
                       if lst[current] > lst[j]:
                       current = j
        if current != j:
                       lst[i], lst[current] = lst[current],lst[i]
