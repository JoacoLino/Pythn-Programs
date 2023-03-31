"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
def mergeTwoLists(list1, list2):
    a = []
    i = 0
    k = 0
    if len(list1) > len(list2):
        min = len(list2)
    else:
        min = len(list1)
    while min > i and min > k:
        if list1[i] == list2[k]:
            a.append(list1[i])
            a.append(list2[k])
            i += 1
            k += 1
        elif list1[i] > list2[k]:
            a.append(list2[k])
            k += 1
        else:
            a.append(list1[i])
            i += 1
    if i < min:
        while i <= min:
            a.append(list1[i])
            i += 1
    else:
        while k <= min:
            a.append(list2[k])
            k += 1
    print(a)
    return a

mergeTwoLists([1,3,4,5],[1,2,4,6,7])