from collections import Counter

def makeStrAnagrams(a, b):
    """
    Given 2 strings, a & b, that may or may not be of the same length, determine the minimum number of characters
    deletions required to make a & b anagrams. Any characters can be deleted from either of the strings.
    :param a: first string
    :param b: second string
    :return: the number of characters to delete to make the 2 strings anagrams of each other.
    """

    aCount = Counter(a)
    bCount = Counter(b)

    cCount = aCount - bCount
    dCount = bCount - aCount

    eCount = cCount + dCount
    return len(list(eCount.elements()))

a = 'hellmshhsjksjcksjkljdksdjfsdjflo0'
b = 'oqxqskodslqùmlleh'

print('Number of characters to delete : ', makeStrAnagrams(a, b))
