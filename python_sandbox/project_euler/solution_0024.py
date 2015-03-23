"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

INITIAL_WORD = '0123456789'

def get_permutations(word):
    results = []

    # the single string has 1 permutation: itself
    if len(word) == 1:
        results.append(word)
        return results
    if len(word) <= 0:
        print "there's a big problem!"

    # loop through all character positions
    for x in range(len(word)):
        # form a simpler word by removing the xth character
        shorter_word = word[0:x] + word[x+1:]

        # generate all permutations of the simpler word
        shorter_word_permutations = get_permutations(shorter_word)

        # add the removed character to the front of each permutation of the shorter word
        for perm in shorter_word_permutations:
            results.append(word[x] + perm)
    return results

if __name__ == '__main__':
    permutations = get_permutations(INITIAL_WORD)
    for x in permutations:
        print x
    print str(len(INITIAL_WORD)) + " letters - " + str(len(permutations)) + " permutations"
    print "The millionth lexicographic permutation is " + permutations[999999]