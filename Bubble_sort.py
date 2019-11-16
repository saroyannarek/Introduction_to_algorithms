def bubble_sort(l):
    for j in l:
        for i in range(1,len(l)):
            if l[i] < l[i-1]:
                l[i-1], l[i] = l[i], l[i-1]
            else:
                continue
    return l
