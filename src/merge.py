"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []  # a new list to copy elements into
    # FIXME: fill out the loop so you merge the lists
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            z.append(x[i])
            i+=1
        elif y[j]>=x[i]:
            i+=1
        else:
            z.append(y[j])
            j+=1

    if j== len(y):
        z=z+x[i:]
    elif i==len(x):
        z=z+y[j:]

    # At least one of the lists is empty now. Copy the
    # remainder of the other into z.
    return z


