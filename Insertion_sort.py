####################################################
# Subject: Insertion sort Algorithm implementation #
# Date: 18/10/2019                                 #
# Author: Narek Saroyan                            #
####################################################

def insertion_sort(list_for_sorting):
    for i in range(1,len(list_for_sorting)):
        key = list_for_sorting[i]
        j = i - 1
        while j >= 0 and list_for_sorting[j] > key:
            list_for_sorting[j+1] = list_for_sorting[j]
            j = j - 1
        list_for_sorting[j+1] = key

    return list_for_sorting
