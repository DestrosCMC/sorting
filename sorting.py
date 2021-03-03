#!/bin/python3

import random


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.

    NOTE:
    In python, helper functions are frequently prepended with the _.
    This is a signal to users of a library that these functions are
    for "internal use only",
    and not part of the "public interface".

    This _merged function could be implemented as a local
    function within the merge_sorted scope rather than a global function.
    The downside of this is that the function can then
    not be tested on its own.
    Typically, you should only implement a function as a local function if
    it cannot function on its own
    (like the go functions from binary search).
    If it's possible to make a function stand-alone,
    then you probably should do that and write test
    cases for the stand-alone function.

    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    if len(ys) == 0:
        return xs
    if len(xs) == 0:
        return ys

    ans = xs + ys
    len_xs = len(xs)
    i = 0
    len_ys = len(ys)
    j = 0
    k = 0

    while i < len_xs and j < len_ys:
        if cmp(xs[i], ys[j]) == -1:
            ans[k] = xs[i]
            i += 1
            k += 1
        else:
            ans[k] = ys[j]
            j += 1
            k += 1

    while i < len_xs:
        ans[k] = xs[i]
        i += 1
        k += 1

    while j < len(ys):
        ans[k] = ys[j]
        j += 1
        k += 1

    return ans


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) <= 1:
        return xs

    arr = xs
    if len(arr) > 1:

        mid = len(arr) // 2

        l, r = arr[:mid], arr[mid:]

        return _merged(merge_sorted(l, cmp),
                       merge_sorted(r, cmp), cmp)

        '''
        i = j = k = 0

        while i < len(l) and j < len(r):
            if cmp_standard(r[i], l[j]) != 1:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr
    '''


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,
    and the list is split into a "less than"
    sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) <= 1:
        return xs

    arr = xs

    if len(arr) > 1:

        pivot = random.randrange(len(xs))

        l, r = arr[:pivot], arr[pivot:]

        return _merged(merge_sorted(l, cmp),
                       merge_sorted(r, cmp), cmp)

    '''
    small = []
    equal = []
    large = []

    if len(xs) > 1:
        pivot = random.randrange(len(xs))
        for x in xs:
            if x < pivot:
                small.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                large.append(x)
        return quick_sorted(small) + equal + quick_sorted(large)
    else:
        return xs
    '''


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented "in-place".
    This means that no extra lists are allocated,
    or that the algorithm uses Theta(1) additional memory.
    Merge sort, on the other hand, must allocate
    intermediate lists for the merge step,
    and has a Theta(n) memory requirement.
    Even though quick sort and merge sort both
    have the same Theta(n log n) runtime,
    this more efficient memory usage typically makes quick
    sort faster in practice.
    (We say quick sort has a lower "constant factor" in its runtime.)
    The downside of implementing quick sort in this way is that it will
    no longer be a
    [stable sort](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability),
    but this is typically inconsequential.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable
    instead of returning a copy of the list.
    '''
    '''
    def partition(xs, begin, end):
        pivot = begin
        for i in range(begin + 1, end + 1):
            pivot += 1
            xs[i], xs[pivot] = xs[pivot], xs[i]
        xs[pivot], xs[begin] = xs[begin], xs[pivot]
        return pivot

    def quicksort(xs, begin=0, end=None):
        if end is None:
            end = len(xs) - 1

        def _quicksort(xs, begin, end):
            if cmp_standard(begin, end) == 1:
                return
            pivot = partition(xs, begin, end)
            _quicksort(xs, begin, pivot - 1)
            _quicksort(xs, pivot + 1, end)
        return _quicksort(xs, begin, end)
    '''
    return
