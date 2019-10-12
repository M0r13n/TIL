"""
Task: Find the nth largest item in a unsorted list.
Example: [1,4,2,9,6] --> n=2 --> searched item is 4.
Naive solution: Sort the list and return the nth item. Sorting takes O(nlogn)
"""
import random
import time


def nth_item(n, arr):
    """
    Idea: We iteratively choose a pivot element and place every item smaller
    that the pivot element before it and every bigger element after it.
    Starting from the full list we iteratively bound the area of the
    array to look at.
    Select the new bounds as follows:
    Case 1: The new index of the selected pivot element equals n:
        Hurrah! We found it.
    Case 2: n ist smaller that the new pivot index:
        We only need to focus on the part between the old lower bound
        and pivot_index -1
    Case 3: n is bigger than the new pivot index:
        We only need to change the lower bound to pivot_index+1 and
        search between this new lower bound and the old upper bound
    Generally this strategy is heavily inspired by Quicksort.
    It`s average runtime should be linear and it`s worstcase runtime
    quadratic.
    Worstcase:  The input list is sorted backwards and pivot is first element.
                n+(n-1)+(n-2)+... <=> sum(n-i) <=> n*n
    Average:    List is evenly distributed. The partitions is consecutively
                splitted into halves and then halves of halves and so on.
                n+ n/2 + n/4 + n/8 = n
    """

    def partition(lower, upper, n, arr):
        """
        Partitions a sub-partition of a list,
        so that for pivot:=arr[p_index]
        and every x in arr[lower:upper]:
        (1) x<pivot -> index(x)<pivot
        (2) x>pivot -> index(x)>pivot
        is true.
        :param lower: lower bound
        :param upper: upper bound
        :param p_index: pivot index
        :param arr: array/list
        :return: partitioned array/list, new index of pivot
        """
        # one element only
        if lower == upper:
            return arr[lower]

        p_index = random.randint(lower, upper)
        # select pivot element
        pivot = arr[p_index]
        # swap pivot and last element
        arr[p_index], arr[upper] = arr[upper], arr[p_index]
        # index, every item with a index smaller than this, is known to be < than pivot
        # that also means that at the end l is the new index for our pivot element
        l = lower

        # for every element
        for m in range(lower, upper):

            # if it is smaller than the pivot
            if arr[m] < pivot:
                # swap it with the pivot
                arr[l], arr[m] = arr[m], arr[l]
                l += 1

        # finally swap the pivot element to its correct position
        arr[upper], arr[l] = arr[l], arr[upper]

        if n == l:
            return arr[n]
        elif n < l:
            # search new bounds
            return partition(lower, l - 1, n, arr)

        else:
            # search new bounds
            return partition(l + 1, upper, n, arr)

    return partition(0, len(arr) - 1, n, arr)


def test(n):
    total_time_a = 0
    total_time_b = 0

    for i in range(n):
        arr = [random.randint(0, 9999) for _ in range(random.randint(1, 9999))]
        j = random.randint(0, len(arr) - 1)

        start = time.time()
        x = nth_item(j, arr)
        total_time_a += time.time() - start

        start = time.time()
        y = sorted(arr)[j]
        total_time_b += time.time() - start
    assert (x == y), "Value mismatch found expected {y} , got {x}".format(y=y, x=x)

    print("Algorithm A took %s s" % total_time_a)
    print("Algorithm B took %s s" % total_time_b)


test(20)

