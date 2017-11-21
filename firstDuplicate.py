def firstDuplicate(a):
    """
    This function finds the first duplicate number for which the second occurrence has the minimal index.
    :param a: the array containing duplicates
    :return: -1 if no duplicates in a else the first duplicate number for which the second occurrence has the
    minimal index.
    """
    # check if there are duplicated items in a : if yes -> proceed, else return -1
    duplicates = [i for i in a if a.count(i) >= 2]

    # if there are some duplicated items:
    if len(duplicates) > 0:
        seen = set()  # initialize an empty set that is used to check if the current element of a has been seen before.
        index = []  # empty list to store the index of the already seen items of a. Hence this list stores the index of
        # a particular item every time it is seen in a, except for the first time.

        for idx, item in enumerate(a):
            if item not in seen:
                seen.add(item)  # first time seeing the item, add it to the seen set
            else:
                index.append(idx)  # already seen, add the index to the list
        return a[index[0]]  # return the first duplicate
    else:
        return -1


a = [2, 3, 3, 1, 5, 2]
print(' First duplicate of ', a, 'is ', firstDuplicate(a))
